#include<iostream>  
using namespace std;  
char pre[] = {1, 2, 3, 4, 5, 6};  
int mid[] = {3, 2, 4, 1, 6, 5};  
void post(int root, int start, int end)     //end = len(post)-1 = len(mid)-1, root = start = 0 
{  
    if(start > end)   
        return ;  
    int i = start;  
    while(i < end && mid[i] != pre[root]) i++;  //��λ���������λ��
    post(root + 1, start, i - 1);  //�ݹ鴦��������
    post(root + 1 + i - start, i + 1, end);  //�ݹ鴦��������
    //cout<<pre[root];  //���ʵ�ǰ���ĸ�
    cout<<mid[i];
}  

int main() 
{  
    post(0, 0, 5);  
    return 0;  
}
