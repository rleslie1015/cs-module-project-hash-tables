# # Use frequency analysis to find the key to ciphertext.txt, and then
# # decode it.

# # Your code here

# with open('ciphertext.txt') as f:
#     words = f.read()

# frequency_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
# 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

# frequency_table = {}

# def decrypt(text):
#     #splitting the text by word
#     word_list = text.split()
#     #creating a list to hold each letter for easy deciphering later
#     letter_list = []
#     #loop through each word
#     for word in word_list:
#         #loop through each letter
#         for letter in word:
#             #if the letter exists in our list, we can decode it
#             if letter.upper() in frequency_list:
#                 #cache the freqeuency depending on if it's there already or not
#                 if letter in frequency_table:
#                     frequency_table[letter] += 1
#                 else:
#                     frequency_table[letter] = 1
#             #if it isn't in our list, add it to the master list of letters as is
#             letter_list.append(letter)
#         #if it isn't the last word, add a space after it
#         if word != word_list[-1]:
#             letter_list.append(" ")
    
#     #sort the letters found by most frequent first, so as to match our frequency_list
#     items = list(frequency_table.items())
#     items.sort(key=lambda e: -e[1])
#     ordered_letters = list(dict(items).keys())
    
#     #list which will hold the letters of our final string
#     decoded_list = []

#     #loop through our list of individual letters
#     for letter in letter_list:
#         #if the letter can be deciphered
#         if letter.upper() in frequency_list:
#             #find it's index, because we sorted the letters found by frequency, we know the index will match the index in frequency_list
#             index = ordered_letters.index(letter)
#             #add the cooresponding decoded letter to the final list
#             decoded_list.append(frequency_list[index])
#         else:
#             #if it isn't decipherable, put it in as is
#             decoded_list.append(letter)

#     #join the final list of letters back into a string
#     final_str = "".join(decoded_list)

#     return final_str

# print(decrypt(words))