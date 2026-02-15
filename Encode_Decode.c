#include<bits/stdc++.h>
using namespace std;
class Solution{

public:



    string  encode(vector<string>&strs){

    string result = "";
    for(string &word:strs){


        result = to_string(word.size()) +'#'+word;
    }
    return result;


    }
    vector<string> decode(string s){


    vector<string>result;
    int i =0;
    while(i<s.size()){


        int j=i;
        while(s[j]!='#'){



            j++;
        }

        int length = stoi(s.substr(i,j-i));
        j++;
        string word = s.substr(j,length);
        result.push_back(word);
        i=j+length;



    }
    return result;

    }
};
int main(){

Solution obj;
int n;
cout<<"Enter a number of strings\n"<<endl;
cin>>n;
cin.ignore();
vector<string>strs;
cout<<"Enter string:\n";
for(int i=0;i<n;i++){
    string s;
    getline(cin,s);
    strs.push_back(s);
}
string encoded  = obj.encode(strs);
cout<<"\n Encoded string:\n"<<encoded<<endl;
vector<string> decoded = obj.decode(encoded);
for(string s: decoded){


    cout<<s<<endl;
}
return 0;
}










