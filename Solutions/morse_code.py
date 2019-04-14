import string


class EnglishToMorse():
    
    def uniqueMorseRepresentations(self, words: [str]) -> int:

        arr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        map_ = dict(zip(string.ascii_lowercase, arr))
        print(map_)
        result = set()

        for word in words:
            value = ""
            for i in word:
                value += arr[ord(i) - ord('a')]
            result.add(value)
        return (len(result))

e = EnglishToMorse()
print(e.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))

print(ord('b'))
