"""
U
 return a dictionary of words and their occurences

P
split the string into array of words
create a dictionary
key = word
value = occurence
loop over the array counting each word 
if word exists in dictionary then increment 
else set with 1

E
R
"""
ignoreChars = ['"', ":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]
ignore = [":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "\""]

def word_count(s):
    dictionary = {}
    # Your code here
    s = s.lower()
    s = ''.join(c for c in s if c not in ignoreChars)
    words = s.split()
    for word in words:
        if word == '':
            return {}
        if word in dictionary:
            dictionary[word] += 1
 
        else:
            dictionary[word] = 1
    return dictionary


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count("Hello    hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))