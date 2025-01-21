import re
#This will read the book
def sort_on(dict):
    for value in dict:
        return dict[value]

def main():
    book1 = 'books/frankenstein.txt'
    with open(book1, 'r') as f:
        file_contents = f.read()
        wordcount = len(file_contents)
        print(wordcount)
        book_to_string = file_contents.lower()
        book_to_string = re.split(r'(\s+)', book_to_string)
        #print(wordcount)
        
        alphabet_list = []
        char_count = {"a": 0, "b": 0, "c": 0, "d": 0,
                      "e": 0, "f": 0, "g": 0, "h": 0,
                      "i": 0, "j": 0, "k": 0, "l": 0,
                      "m": 0, "n": 0, "o": 0, "p": 0,
                      "q": 0, "r": 0, "s": 0, "t": 0,
                      "u": 0, "v": 0, "w": 0, "x": 0,
                      "y": 0, "z": 0, " ": 0, "'": 0,
                      ".": 0, ",": 0, ":": 0, ";": 0,
                      ")": 0, "(": 0, "-": 0, "1": 0,
                      "2": 0, "3": 0, "4": 0, "5": 0,
                      "6": 0, "7": 0, "8": 0, "9": 0,
                      "0": 0, "[": 0, "]": 0, "{": 0,
                      "}": 0, "#": 0, "*": 0, "?": 0,
                      "!": 0, '"': 0, "'": 0, "_": 0,
                      "/": 0, "%": 0, "@": 0, "$": 0,
                      "\n": 0}
        for char in book_to_string:
            char_list = []
            char_list = list(char)
            for add_this_char in char_list:
                char_count[add_this_char] +=1
        print(f"--- Begin report of {book1} ---")
        print(f"{wordcount} words found in the document")
        for dic_char in char_count:
            if dic_char.isalpha() == True:
                alphabet_count = {}
                alphabet_count.setdefault(dic_char, char_count[dic_char])
                alphabet_list.append(alphabet_count)
        alphabet_list.sort(reverse=True, key=sort_on)
        for value in alphabet_list:
            for key in value:
                print(f"The '{key}' character was found {value[key]}")  
        print("--- End report ---")           

main()