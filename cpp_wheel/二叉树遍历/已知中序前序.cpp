#include<iostream>  
using namespace std;  
char pre[] = {1, 2, 3, 4, 5, 6};  
int mid[] = {3, 2, 4, 1, 6, 5};  
void post(int root, int start, int end)     //end = len(post)-1 = len(mid)-1, root = start = 0 
{  
    if(start > end)   
        return ;  
    int i = start;  
    while(i < end && mid[i] != pre[root]) i++;  //定位根在中序的位置
    post(root + 1, start, i - 1);  //递归处理左子树
    post(root + 1 + i - start, i + 1, end);  //递归处理右子树
    //cout<<pre[root];  //访问当前树的根
    cout<<mid[i];
}  

int main() 
{  
    post(0, 0, 5);  
    return 0;  
}
