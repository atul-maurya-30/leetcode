class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        #lets create a dictionary for transformation
        d={"a":"b","b":"c","c":"d","d":"e","e":"f","f":"g","g":"h","h":"i","i":"j","j":"k","k":"l","l":"m","m":"n","n":"o","o":"p","p":"q","q":"r",'r':'s','s':'t','t':'u','u':'v','v':'w','w':'x','x':'y','y':'z','z':'a'}

        #use two pointers approach
        i,j=0,0
        # start while loop for checking that subsequence
        while i<len(str1) and j<len(str2):
            #check if current character matches and it is valis transformation
            if str1[i]==str2[j] or d[str1[i]]==str2[j]:
                j+=1 #move to next character in str2
            i+=1 #move to next character in str1
        return j==len(str2) #if after while loop, length of j is equal to lenght of str2 then return True else False

        