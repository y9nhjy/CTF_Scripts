#include <stdio.h>
#include <stdint.h>

//加密函数
void encrypt(unsigned int num_rounds, uint32_t* v, uint32_t* k) {
	uint32_t v0 = v[0], v1 = v[1], v2 = v[2], v3 = v[3],v4 = v[4], v5 = v[5],v6 = v[6], v7 = v[7],sum = 0;
    int v15,v17=12;
	do{
        sum -= 0x61C88647;

        v0 += ((sum ^ v1) + (k[(sum >> 2) & 3] ^ v7)) ^ (((16 * v7) ^ (v1 >> 3)) + ((v7 >> 5) ^ (4 * v1)));
        v[0] = v0;

        v1 += ((k[(sum >> 2) & 3 ^ 1] ^ v0) + (sum ^ v2)) ^ (((16 * v0) ^ (v2 >> 3)) + ((v0 >> 5) ^ (4 * v2)));
        v[1] = v1;

        v2 += ((sum ^ v3) + (k[(sum >> 2) & 3 ^ 2] ^ v1)) ^ (((16 * v1) ^ (v3 >> 3)) + ((v1 >> 5) ^ (4 * v3)));
        v[2] = v2;

        v3 += ((sum ^ v4) + (k[(sum >> 2) & 3 ^ 3] ^ v2)) ^ (((16 * v2) ^ (v4 >> 3)) + ((v2 >> 5) ^ (4 * v4)));
        v[3] = v3;

        v4 += ((sum ^ v5) + (k[(sum >> 2) & 3] ^ v3)) ^ (((16 * v3) ^ (v5 >> 3)) + ((v3 >> 5) ^ (4 * v5)));
        v[4] = v4;

        v5 += ((k[(sum >> 2) & 3 ^ 1] ^ v4) + (sum ^ v6)) ^ (((16 * v4) ^ (v6 >> 3)) + ((v4 >> 5) ^ (4 * v6)));
        v[5] = v5;

        v6 += (((sum ^ v7) + (k[(sum >> 2) & 3 ^ 2] ^ v5)) ^ (((16 * v5) ^ (v7 >> 3)) + ((v5 >> 5) ^ (4 * v7))));
        v[6] = v6;

        v7 += (((sum ^ v0) + (k[(sum >> 2) & 3 ^ 3] ^ v6))) ^ (((16 * v6) ^ (v0 >> 3))+ ((v6 >> 5) ^ (4 * v0)));
        v[7] = v7;

        v15 = v17-- == 1;

    }while(!v15);
    printf("sum==0x%x\n",sum);
}

//解密函数
void decrypt(unsigned int num_rounds, uint32_t* v, uint32_t* k) {
	uint32_t v0 = v[0], v1 = v[1], v2 = v[2], v3 = v[3],v4 = v[4], v5 = v[5],v6 = v[6], v7 = v[7],sum = 0x6a99b4ac;
    int v15,v17=12;
	do{

        v7 -= (((sum ^ v0) + (k[(sum >> 2) & 3 ^ 3] ^ v6))) ^ (((16 * v6) ^ (v0 >> 3))+ ((v6 >> 5) ^ (4 * v0)));
        v[7] = v7;

        v6 -= (((sum ^ v7) + (k[(sum >> 2) & 3 ^ 2] ^ v5)) ^ (((16 * v5) ^ (v7 >> 3)) + ((v5 >> 5) ^ (4 * v7))));
        v[6] = v6;

        v5 -= ((k[(sum >> 2) & 3 ^ 1] ^ v4) + (sum ^ v6)) ^ (((16 * v4) ^ (v6 >> 3)) + ((v4 >> 5) ^ (4 * v6)));
        v[5] = v5;

        v4 -= ((sum ^ v5) + (k[(sum >> 2) & 3] ^ v3)) ^ (((16 * v3) ^ (v5 >> 3)) + ((v3 >> 5) ^ (4 * v5)));
        v[4] = v4;

        v3 -= ((sum ^ v4) + (k[(sum >> 2) & 3 ^ 3] ^ v2)) ^ (((16 * v2) ^ (v4 >> 3)) + ((v2 >> 5) ^ (4 * v4)));
        v[3] = v3;

        v2 -= ((sum ^ v3) + (k[(sum >> 2) & 3 ^ 2] ^ v1)) ^ (((16 * v1) ^ (v3 >> 3)) + ((v1 >> 5) ^ (4 * v3)));
        v[2] = v2;

        v1 -= ((k[(sum >> 2) & 3 ^ 1] ^ v0) + (sum ^ v2)) ^ (((16 * v0) ^ (v2 >> 3)) + ((v0 >> 5) ^ (4 * v2)));
        v[1] = v1;

        v0 -= ((sum ^ v1) + (k[(sum >> 2) & 3] ^ v7)) ^ (((16 * v7) ^ (v1 >> 3)) + ((v7 >> 5) ^ (4 * v1)));
        v[0] = v0;

        sum += 0x61C88647;

        v15 = v17-- == 1;

    }while(!v15);
    printf("sum==0x%x\n",sum);
}

//打印数据 hex_or_chr: 1-hex 0-chr
void dump_data(uint32_t * v,int n,bool hex_or_chr)
{
	if(hex_or_chr)
	{
		for(int i=0;i<n;i++)
		{
			printf("0x%x,",v[i]);
		}
	}
	else
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < sizeof(uint32_t)/sizeof(uint8_t); j++)
			{
				printf("%c", (v[i] >> (j * 8)) & 0xFF);
			}
		}
	}
	printf("\n");
	return;
}

int main()
{
	// v为要加解密的数据
	uint32_t v[] = { 0x10bd3b47,0x6155e0f9,0x6af7ebc5,0x8d23435f,0x1a091605,0xd43d40ef,0xb4b16a67,0x6b3578a9 };
	// k为加解密密钥
	uint32_t k[6] = { 0x1234, 0x2345, 0x4567, 0x6789, 0, 0 };
	// num_rounds，建议取值为32
	unsigned int r = 32;

	int n = sizeof(v) / sizeof(uint32_t);
	/*
	printf("加密前明文数据：");
	dump_data(v,n,1);
    
	for(int i=0;i<n/2;i++)
	{
		encrypt(r,&v[i*2], k);
	}
    */
	printf("加密后密文数据：");
	dump_data(v,n,1);
    /*
	for(int i=0;i<n/2;i++)
	{
		decrypt(r,&v[i*2], k);
	}
    */
    decrypt(0,v,k);
	printf("解密后明文数据：");
	dump_data(v,n,1);

	printf("解密后明文字符：");
	dump_data(v,n,0);

	return 0;
}

// 7f943921724d63dc0ac9c6febf99fa88

