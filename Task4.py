#Question:1 (LUHN algorithm)
def luhn_check(card_number):
    # Convert number into list of integers
    digits = [int(d) for d in str(card_number)]

    digits.reverse()
    
    total = 0
    
    for i in range(len(digits)):
        if i % 2 == 1:  # Double every second digit
            doubled = digits[i] * 2
            if doubled > 9:
                doubled -= 9
            total += doubled
        else:
            total += digits[i]

    return total % 10 == 0

#input
card = input("Enter card number: ")
if luhn_check(card):
    print("Valid Card Number")
else:
    print("Invalid Card Number")

#--------------------------------------------------------------------

#Question:2 (remove punctuations)

import string

text = input("Enter a string: ")

# Remove punctuation
clean_text = ""

for char in text:
    if char not in string.punctuation:
        clean_text += char

print("String without punctuation:")
print(clean_text)

#--------------------------------------------------------------------

#Question:3 (alphabetic order)

sentence = input("Enter a sente

sentence = sentence.lower()

words = sentence.split()

words.sort()

print("Sentence in alphabetical order:")
for word in words:
    print(word)

