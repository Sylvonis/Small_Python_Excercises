
"""
    Create a program that reads a file and creates a dictionary in which each key
    is a word and each value is the number and occurrences in the file
"""

word_dict = {}

with open("default_text.txt", "r") as text_file:
    for line in text_file:
        word_list = line.lower().split()
        POINTER = 0
        for word in word_list:
            if not word.isalnum():
                newWord = ""
                for char in word:
                    if char.isalnum() or char in word[1:-2]:
                        newWord += char
                    else:
                        word.replace(char, "")
                word = newWord
                word_list[POINTER] = word[:-1]
                word_dict[word_list[POINTER]] = 1
            elif word not in word_dict:
                word_dict[word] = 1
                # print(f"{word}: first time in")
            elif word in word_dict:
                word_dict[word] += 1
            POINTER += 1

    print({k: v for k, v in sorted(word_dict.items(), key=lambda item: item[1], reverse=True)})
