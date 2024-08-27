#include <idc.idc>
#define PT_LOAD              1
#define PT_DYNAMIC           2

static main(void){
    // 定义要 dump 的起始地址和结束地址
    auto start_addr = 0x666666;
    auto end_addr = 0x666666 + 0x6666;
    
    // 定义输出文件路径
    auto output_file = "C:\\Users\\user01\\Desktop\\1.bin";
    
    // 打开输出文件
    auto file = fopen(output_file, "wb");
    
    // 读取内存并写入文件
    auto addr;
    for (addr = start_addr; addr < end_addr; addr++) {
        auto byte = Byte(addr);
        fputc(byte, file);
    }
    
    // 关闭文件
    fclose(file);
    
    Message("Dump completed successfully.\n");
}
