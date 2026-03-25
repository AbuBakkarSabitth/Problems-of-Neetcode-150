#include<bits/stdc++.h>
using namespace std;


class Solution{

public:
    vector<int> dailyTemperatures(vector<int>& temperatures){
          int n = temperatures.size();
          vector<int>result(n,0);
          stack<int>st;
          for(int i=0;i<n;i++){
                while(!st.empty() && temperatures[i] > temperatures[st.top()]){
                int prevIndex = st.top();
                st.pop();
                result[prevIndex] = i-prevIndex;

          }
          st.push(i);
    }
    return result;
}
};
int main(){

    int n;
    cin>>n;
    vector<int>temperatures(n);
    for(int i=0;i<n;i++){
        cin>>temperatures[i];
    }
    vector<int>result;
    Solution s;
    result= s.dailyTemperatures(temperatures);
    for(int r:result){
        cout<<r<<endl;
    }




}

