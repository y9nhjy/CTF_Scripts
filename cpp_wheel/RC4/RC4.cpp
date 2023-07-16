#include<stdio.h>

//RC4初始化函数
void rc4_init(unsigned char* s, unsigned char* key, unsigned long key_len){
	unsigned int i = 0, j = 0;
	char k[256] = { 0 };
	unsigned char tmp = 0;
	for (i = 0; i < 256; i++) {
		s[i] = i;
		k[i] = key[i % key_len];
	}
	for (i = 0; i < 256; i++) {
		j = (j + s[i] + k[i]) % 256;
		tmp = s[i];
		s[i] = s[j];
		s[j] = tmp;
	}
}

/*
RC4加解密函数
unsigned char* Data     加解密的数据
unsigned long data_len     加解密数据的长度
unsigned char* key      密钥
unsigned long key_len     密钥长度
*/
void rc4_crypt(unsigned char* s, unsigned char* Data, unsigned long data_len){
	int i = 0, j = 0, t = 0;
	unsigned long k = 0;
	unsigned char tmp;
	for (k = 0; k < data_len; k++) {
		i = (i + 1) % 256;
		j = (j + s[i]) % 256;
		tmp = s[i];
		s[i] = s[j];
		s[j] = tmp;
		t = (s[i] + s[j]) % 256;
		Data[k] = Data[k] ^ s[t];
	}
}

int main(){
	//字符串密钥
	unsigned char key[] = "CISCN_easy_reverse";
	unsigned long key_len = sizeof(key) - 1;
	/*
	//数组密钥
	unsigned char key[] = {0x01,0x23,0x45,0x67,0x89,0xab,0xcd,0xef,0xfe,0xdc,0xba,0x98,0x76,0x54,0x32,0x10};
	unsigned long key_len = sizeof(key);
    */
	unsigned char s[256];
	rc4_init(s, key, key_len);
	//加解密数据
	unsigned char data[] = {0x31,0x31,0x31,0x31,0x31,0x31,0x31,0x31 };
	//加解密
	rc4_crypt(s, data, sizeof(data));

	for (int i = 0; i < sizeof(data); i++){
		printf("%x ", data[i]);
	}
	return 0;
}

