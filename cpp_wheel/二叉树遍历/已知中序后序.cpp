#include<iostream>  
using namespace std;  
char* post = "20f0Th{2tsIS_icArE}e7__w";  
char* mid = "2f0t02T{hcsiI_SwA__r7Ee}";  
void pre(int root, int start, int end)   //root = end = len(post)-1 = len(mid)-1, start = 0 
{  
    if(start > end)   
        return ;  
    int i = start;  
    while(i < end && mid[i] != post[root]) i++;  //��λ���������λ��
    cout<<mid[i];  //���ʵ�ǰ��������ĸ�
    pre(root-1-(end-i), start, i - 1);  //�ݹ鴦��������
    pre(root-1, i + 1, end);  //�ݹ鴦��������  
}  

int main()
{  
    pre(23, 0, 23);  
    return 0;  
}
