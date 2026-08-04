class Solution:

    def encode(self, strs: List[str]) -> str:
        #encoded_string = ""
        #for word in strs:
         #   encoded_string += str(len(word))+ "#" + word
        #print(encoded_string)
        
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        #n = len(s)
        i = 0
        while i<len(s):
            j = i
            while s[j] != "#":
                j+=1
            
            length = int(s[i:j])
            i = j+1
            j = i+length
            decoded_strs.append(s[i:i+length])
            i+=length
        return decoded_strs
