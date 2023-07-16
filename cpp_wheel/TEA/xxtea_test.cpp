#include<stdio.h>
#include<stdint.h>
//#define MX (((z>>5^y<<2)+(y>>3^z<<4))^((sum^y)+(key[(p&3)^e]^z)))
#define MX (((z>>4^y<<2)+(y>>3^z<<5))^((sum^y)+(key[(e^p&3)]^z)))
//#define DELTA 0x9e3779b9
#define DELTA 0x11451400
//delta=0x61C88647=-(0x9e3779b)

//����
void xxtea(uint32_t* v,int n,uint32_t const key[4]){
	uint32_t y,z,sum;
	unsigned p,rounds,e;
	if(n>1){
		rounds=6+52/n;
		sum=0;
		z=v[n-1];
		do{
			sum+=DELTA;
			e=(sum>>2)&3;
			for(p=0;p<n-1;p++){
				y=v[p+1];
				v[p]+=MX;
				z=v[p];
			}
			y=v[0];
			v[n-1]+=MX;
			z=v[n-1];
		}
		while(--rounds);
	}
	else if(n<-1){
		n=-n;
		rounds=6+52/n;
		sum=DELTA*rounds;
		y=v[0];
		do{
			e=(sum>>2)&3;
			for(p=n-1;p>0;p--){
				z=v[p-1];
				v[p]-=MX;
				y=v[p];
			}
			z=v[n-1];
			v[0]-=MX;
			y=v[0];
			sum-=DELTA;
		}
		while(--rounds);
	}
}

int main(){
	uint32_t v[]={0x38FA8A82,0xD7501380,0x0E40969D,0x4E169120,0x713A29AB,0x6CE5393D,0xB69D752E,0x841A88E6,0x6F31B459};
//	uint32_t const k[4]={0x1234,0x2345,0x4567,0x6789};
	uint32_t const k[4]={0x19,0x19,0x08,0x10};
	//n=bit(v)/32,������ʾ����,������ʾ����
	int n=sizeof(v)/sizeof(v[0]);
	printf("n = %d\n",n);
//	v:���� ___bit
//	k:��Կ 128bit
//	printf("����:%u %u\n",v[0],v[1]);
//	xxtea(v,n,k);
//	printf("���ܺ�:\n");
//	for(int i=0;i<n;i++){
//		printf("%8x",v[i]);
//	}
	xxtea(v,-n,k);
	printf("���ܺ�:\n");
	for(int i=0;i<n;i++){
		printf("%8x",v[i]);
	}
}
