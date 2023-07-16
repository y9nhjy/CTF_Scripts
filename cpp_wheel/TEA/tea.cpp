#include <stdio.h>
#include <stdint.h>
 
void encrypt (uint32_t* v, uint32_t* k) {
    uint32_t v0=v[0], v1=v[1], sum=0, i;
    uint32_t delta=0x9e3779b9;
    uint32_t k0=k[0], k1=k[1], k2=k[2], k3=k[3];
    for (i=0; i < 32; i++) {
        sum += delta;
        v0 += ((v1<<4) + k0) ^ (v1 + sum) ^ ((v1>>5) + k1);
        v1 += ((v0<<4) + k2) ^ (v0 + sum) ^ ((v0>>5) + k3);
    }
    v[0]=v0; v[1]=v1;
}
 
void decrypt (uint32_t* v, uint32_t* k) {
    uint32_t v0=v[0], v1=v[1], i;
    uint32_t delta=0x9e3779b9;
    uint32_t sum = delta*32;
    uint32_t k0=k[0], k1=k[1], k2=k[2], k3=k[3];
    for (i=0; i<32; i++) {
        v1 -= ((v0<<4) + k2) ^ (v0 + sum) ^ ((v0>>5) + k3);
        v0 -= ((v1<<4) + k0) ^ (v1 + sum) ^ ((v1>>5) + k1);
        sum -= delta;
    }
    v[0]=v0; v[1]=v1;
}
 
int main()
{
//    uint32_t enflag[] = {0xCE21E888,0x709D000B,0x8FE6B191,0x96EA3101,0x7D9D20A3,0xFB7D18A9,0xCAC552C4,0x536769A9};
    uint32_t enflag[] = {0x60FCDEF7,0x0236DBEC};
    uint32_t key[4] = {0x00000012, 0x00000034, 0x00000056, 0x00000078};
    for(int i=0;i<sizeof(enflag)/sizeof(enflag[0]);i+=2)
    {
        uint32_t temp[2];        //定义来解密
        temp[0] = enflag[i];
        temp[1] = enflag[i+1];
        decrypt(temp, key);
//        printf("%X %X\n",temp[0],temp[1]);
        printf("%c%c%c%c%c%c%c%c",*((char*)&temp[0]+0),*((char*)&temp[0]+1),*((char*)&temp[0]+2),*((char*)&temp[0]+3),*((char*)&temp[1]+0),*((char*)&temp[1]+1),*((char*)&temp[1]+2),*((char*)&temp[1]+3));
    }
    return 0;
}
