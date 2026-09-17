
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <random>
#include <cmath>
#include <cctype>
#include <ctime>
using namespace std;

string alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ";

string normalize(string s){
    for(char &c:s) c=toupper(c);
    return s;
}

string encrypt(string text,string key){
    string r=text;
    for(int i=0;i<r.size();i++){
        char c=toupper(r[i]);
        if(c>='A'&&c<='Z') r[i]=key[c-'A'];
    }
    return r;
}

string decrypt(string text,string key){
    string r=text;
    for(int i=0;i<r.size();i++){
        char c=toupper(r[i]);
        if(c>='A'&&c<='Z'){
            int p=key.find(c);
            r[i]=alphabet[p];
        }
    }
    return r;
}

void frequency_analysis(string text){
    map<char,int> f;
    int total=0;
    for(char c:text){
        c=toupper(c);
        if(c>='A'&&c<='Z'){
            f[c]++;
            total++;
        }
    }
    vector<pair<char,int>> v(f.begin(),f.end());
    sort(v.begin(),v.end(),[](auto &a,auto &b){
        return a.second>b.second;
    });
    cout<<"\nFrequency Analysis\n";
    for(auto p:v)
        cout<<p.first<<" "<<p.second<<" "
        <<100.0*p.second/total<<"%\n";
}

vector<string> words(string text){
    vector<string> v;
    string w="";
    for(char c:text){
        if(isalpha(c)) w+=toupper(c);
        else if(w!=""){
            v.push_back(w);
            w="";
        }
    }
    if(w!="") v.push_back(w);
    return v;
}

void word_frequency_analysis(string text){
    map<string,int> f;
    for(string w:words(text)) f[w]++;
    cout<<"\nWord Frequency Analysis\n";
    for(auto p:f) cout<<p.first<<" "<<p.second<<"\n";
}

string pattern_analysis_word(string w){
    map<char,int> m;
    string r="";
    int n=0;
    for(char c:w){
        if(!m.count(c)) m[c]=n++;
        r+=to_string(m[c]);
    }
    return r;
}

void pattern_analysis(string text){
    cout<<"\nPattern Analysis\n";
    for(string w:words(text))
        cout<<w<<" -> "<<pattern_analysis_word(w)<<"\n";
}

string apply_substitution(string text,string key){
    return decrypt(text,key);
}

void display_partial_plaintext(string text,string key){
    cout<<"\nPartial Plaintext\n";
    cout<<decrypt(text,key)<<"\n";
}

double score_text(string text){
    map<string,double> common={
        {"THE",5},{"AND",4},{"ING",4},{"ION",3},{"THAT",3},
        {"THIS",3},{"WITH",3},{"FOR",3},{"ARE",3},{"NOT",2},
        {"FROM",2},{"CRYPT",4},{"DATA",2},{"SECURITY",3},
        {"OF",2},{"TO",2},{"IN",2},{"IS",2},{"A",2}
    };
    double score=0;
    for(string w:words(text)){
        if(common.count(w)) score+=common[w];
    }
    for(int i=0;i+2<text.size();i++){
        string s="";
        for(int j=0;j<3;j++){
            char c=toupper(text[i+j]);
            if(c>='A'&&c<='Z') s+=c;
        }
        if(s=="THE") score+=5;
        if(s=="AND") score+=4;
        if(s=="ING") score+=4;
    }
    return score;
}

string random_key(mt19937 &rng){
    string k=alphabet;
    shuffle(k.begin(),k.end(),rng);
    return k;
}

string hill_climb(string cipher){
    mt19937 rng(time(0));
    string bestkey=random_key(rng);
    double bestscore=score_text(decrypt(cipher,bestkey));
    for(int restart=0;restart<150;restart++){
        string key=random_key(rng);
        double score=score_text(decrypt(cipher,key));
        for(int iter=0;iter<3000;iter++){
            int a=rng()%26,b=rng()%26;
            swap(key[a],key[b]);
            double ns=score_text(decrypt(cipher,key));
            if(ns>=score){
                score=ns;
            }else{
                swap(key[a],key[b]);
            }
            if(score>bestscore){
                bestscore=score;
                bestkey=key;
            }
        }
    }
    return bestkey;
}

bool verify_solution(string plaintext,string ciphertext,string key){
    return encrypt(plaintext,key)==ciphertext;
}

int main(){
    ifstream file("testcases/plaintext.txt");
    string plaintext((istreambuf_iterator<char>(file)),{});
    if(plaintext.empty()){
        cout<<"Plaintext file is empty or missing\n";
        return 0;
    }

    mt19937 rng(time(0));
    string key=random_key(rng);
    string ciphertext=encrypt(plaintext,key);

    cout<<"Original Plaintext:\n"<<plaintext<<"\n";
    cout<<"\nSubstitution Key:\n"<<key<<"\n";
    cout<<"\nCiphertext:\n"<<ciphertext<<"\n";

    frequency_analysis(ciphertext);
    word_frequency_analysis(ciphertext);
    pattern_analysis(ciphertext);

    cout<<"\nRecovering Key...\n";
    string recovered=hill_climb(ciphertext);

    cout<<"\nRecovered Key:\n"<<recovered<<"\n";
    display_partial_plaintext(ciphertext,recovered);

    string recovered_plaintext=decrypt(ciphertext,recovered);
    cout<<"\nRecovered Plaintext:\n"<<recovered_plaintext<<"\n";

    string verified=encrypt(recovered_plaintext,recovered);
    cout<<"\nVerification: ";
    if(verified==ciphertext) cout<<"PASS\n";
    else cout<<"FAIL\n";

    return 0;
}
