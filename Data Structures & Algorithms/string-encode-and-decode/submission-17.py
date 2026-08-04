class Solution:

    def encode(self, strs: List[str]) -> str:
        #encoded_string = ""
        #for word in strs:
         #   encoded_string += str(len(word))+ "#" + word
        #print(encoded_string)
        
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        n = len(s)
        i = 0

        while i<n:
            
            length_string = ""
            while i<n and s[i].isdigit()  and s[i]!= "#":
                length_string +=s[i]
                i+=1
            i+=1
            print("i = ", i, " length = ", length_string)
            length = int(length_string)
            decoded_strs.append(s[i:i+length])
            i+=length
        return decoded_strs
