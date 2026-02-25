
#include<bits/stdc++.h>
using namespace std;
class Solution{
public:
    bool isPalindrome(string s){
    int left =0;
    int right = s.size()-1;
    while(left<right){

        while(left<right && !isalnum(s[left])){
            left++;
        }
        while(left <right && !isalnum(s[right])){
            right--;
        }
        if(tolower(s[left])!= tolower(s[right])){
            return false;
        }
        left++;
        right--;

    }
    return true;


    }


};
int main(){

Solution s;
string in;

getline(cin,in);
bool result  = s.isPalindrome(in);
if(result ==0){
    cout<<"Is not palindrome"<<endl;
}
else{
    cout<<"Is palindrome"<<endl;
}




}

