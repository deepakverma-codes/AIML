# Number of vowel in any word
name = 'Deepak Verma'
vowel = 0
for ch in name:
    if(ch == 'a' or ch == 'A'or ch == 'e' or ch == 'E'or ch == 'i' or ch == 'I' or ch == 'o' or ch == 'O' or ch == 'u' or ch == 'U'):
        vowel += 1
print(f"Total Vowel in {name} are {vowel}")        