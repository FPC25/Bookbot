import os
  
def countChar(text):
    
    values_set = set()
    chars = {}
    for word in text.lower():
        for char in word:   
            if char not in values_set:
                chars[char] = 1
                values_set.add(char)
            else:
                chars[char] += 1

    return dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))

def countWords(text):
    return len(text.split())
    
def getText(text_path):
    with open(text_path) as f:
        file_contents = f.read()
        
    return file_contents



def bookReport(book, num_words, char_counting):
    print(f"--- Begin report of books/{book}.txt ---")
    print(f"{num_words} words found in the document.\n")
    for key in char_counting.keys():
        if key.isalpha():
            print(f"The '{key}' character was found {char_counting[key]} times")
    print("--- End report ---")
def main():
    pwd  = os.getcwd()
    book = "frankenstein"
    contents = getText(f"{pwd}/books/{book}.txt")
    num_words = countWords(contents)
    char_counting = countChar(contents)
    bookReport(book, num_words, char_counting)
    

if __name__ == "__main__":
    main()