import os

def count_words(text):
    words = text.split()
    print(len(words))

def main():
    pwd  = os.getcwd()
    with open(f"{pwd}/books/frankenstein.txt") as f:
        file_contents = f.read()
        count_words(file_contents)

if __name__ == "__main__":
    main()