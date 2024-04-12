#include <idc.idc>
#define PT_LOAD              1
#define PT_DYNAMIC           2
static main(void)
{
        auto ImageBase,StartImg,EndImg;
        auto i,dumpfile;
        StartImg=0x19B11F51440;
        EndImg=0x19B11F51440 + 0xFA00;
        if(dumpfile = fopen("D:\\DumpFile","wb"))
        {

            dump(dumpfile,StartImg,EndImg);
            fclose(dumpfile);
        }

}
static dump(dumpfile,startimg,endimg)
{
        auto i;
        auto size;
        size = endimg-startimg;
        for ( i=0; i < size; i=i+1 )
        {
                fputc(Byte(startimg+i),dumpfile);
        }
}
