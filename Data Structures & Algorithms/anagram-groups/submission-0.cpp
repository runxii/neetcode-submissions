class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        int strsLen = strs.size();
        string safeword = "safe_word";

        if (strsLen<=1)
            result.push_back(strs);
        else{
            for(int i=0;i<strs.size();i++){
                if(strs[i]==safeword){continue;}
                else{
                    vector<string> group;
                    group.push_back(strs[i]);
                    for(int j=i+1;j<strs.size();j++){
                        if(strs[j]==safeword){
                            continue;
                        }
                        else{
                        string stri=strs[i];
                        string strj=strs[j];
                        sort(stri.begin(),stri.end());
                        sort(strj.begin(),strj.end());

                        if(stri == strj){
                            group.push_back(strs[j]);
                            strs[j]=safeword;
                        }}
                    }
                result.push_back(group);}
            }
        }

        return result;
    }
};
