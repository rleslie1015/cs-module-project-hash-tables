"""
UPER! 

Undersand:
    use freq analysis to create a key to use to decode encrypted msg 
    
Plan
    step 1: count all letters in encrypted msg

    step 2: map most frequent letter to most used letter in english language etc

    step 3: use map as key to decode and return decoded msg

    step 4: test code and optimize runtime

Execute

Review 

"""

f = open('ciphertext.txt', 'r')

content = f.read()

total_word_count = len(content.split())
print('total number of words: ', total_word_count)

def letter_count(s):
    d = {}
    for c in s:
        if not c.isalpha():
            continue
        """
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
        """
        if c not in d:
            d[c] = 0
        d[c] += 1
    return d

print(letter_count(content))