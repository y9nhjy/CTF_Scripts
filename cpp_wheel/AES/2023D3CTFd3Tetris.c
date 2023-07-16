#include <stdio.h>
#include <string.h>
#include <stdint.h>

#define CBC 1

#include "aes.h"

int main() {
        uint8_t plaintxt[48] = { 166, 98, 46, 98, 247, 122, 195, 92, 107, 245, 116, 68, 109, 138, 246, 178, 164, 132, 68, 240, 247, 142, 161, 208, 221, 9, 198, 98, 39, 8, 116, 233 };
        uint8_t rc4_key[32] = { 0xe5,0xc5,0xc8,0x6f,0xd4,0x04,0x84,0x75,0x0f,0x46,0xcd,0xca,0x65,0x7d,0x9a,0x7c,0x37,0x04,0x3c,0x56,0xec,0x4c,0x9a,0xe2,0xb8,0x31,0xa3,0x81,0x88,0x25,0x8b,0x10 };
        for (int i = 0; i < 32; i++) {
                plaintxt[i] ^= rc4_key[i];
        }
        uint8_t key[32] = "A SIMPLE KEY!!!!!!!!!!!!!!!!!!!!";
        uint8_t iv[16] = "3d354e98963a69b2";

        struct AES_ctx ctx;

        AES_init_ctx_iv(&ctx, key, iv);
        AES_CBC_decrypt_buffer(&ctx, plaintxt, 32);
        printf("%s", plaintxt);
}
