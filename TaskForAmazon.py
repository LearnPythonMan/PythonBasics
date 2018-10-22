#Find longest substring of "string" where there is no more unique letter than "lenght"

a = 'eiorjfoerifjkerfhorifjierofjiewrojweoifjwefiojewfiowjfoiwejfoiwejoewifjewiofkkiewopfiewopfkewopfkwepofkweopfkweopkfpowefk'
b = 6

c = 'abbbbbbbbcbbbbbzb'
d = 2

def findSubstring(string,lenght):
    longestSubstring = ''
    duplicatesCounter = 1
    for i, letter in enumerate(string):
        substring = letter
        for nextletter in string[i:]:
            if nextletter not in substring:
                duplicatesCounter += 1
            if duplicatesCounter > lenght:
                break
            substring += nextletter
        if len(substring) > len(longestSubstring):
            longestSubstring = substring
        duplicatesCounter = 1
    return longestSubstring

print(findSubstring(a,b))
