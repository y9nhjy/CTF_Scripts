#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "md5.h"

//gcc -c animals_check.c md5_animals.c && gcc -o animals_check animals_check.o md5_animals.o && ./animals_check

unsigned char target[16] = {
    0xDD, 0xB2, 0x6D, 0xF3, 0xE6, 0x0A, 0xC7, 0x83, 0x4A, 0x93, 0x50, 0xB4, 0xA4, 0x59, 0xAB, 0x0E
};
void md5_enc(unsigned char encrypt[]){
    int i;
    unsigned char decrypt[16];
	MD5_CTX md5;
	MD5Init(&md5);
	MD5Update(&md5,encrypt,strlen((char *)encrypt));
	MD5Final(&md5,decrypt);
    //printf("%s\n",encrypt);
	for(i=0;i<16;i++)
	{
		if(target[i]!=decrypt[i]){
            return;
        }
	}
    printf("%s\n",encrypt);
    exit(2);

}
void printCombinations(char* str, int index) {
    if (index == 9) {
        //printf("%s\n", str);
        md5_enc(str);
        return;
    }

    char* animal[] = { "cat", "dog", "fox", "panda", "dragon","monkey" };
    for (int i = 0; i < 6; i++) {
        strncat(str,animal[i],strlen(animal[i]));
        //strcat(str,animal[i]);
        //printf("%c\n",str[0]);
        printCombinations(str, index + 1);
        str[strlen(str) - strlen(animal[i])] = '\0';
    }
}
int main(int argc, char *argv[])
{
    char str[60];
    str[0] = '\0';
    printCombinations(str, 0);
	return 0;
}
