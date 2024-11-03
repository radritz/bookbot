filepath = "books/frankenstein.txt"


def main():
    with open(filepath) as file:
        content = file.read()
    words = count_words(content)
    characters_dict = count_characters(content)
    print_report(words=words, chars=characters_dict)


def count_words(paragraphs: str):
    words = paragraphs.split()
    return len(words)


def count_characters(string: str):
    character_dict = {}
    lower_case_string = string.lower()
    for char in lower_case_string:
        if char.isalpha():
            if character_dict.get(char) is None:
                character_dict[char] = 1
            else:
                character_dict[char] += 1
    return character_dict


def print_report(words: int, chars: dict):
    print(f"--- Begin report of {filepath} ---")
    print(f"{words} words found in the document\n")
    for char in chars:
        print(f"The '{char}' character was found {chars[char]} times ")
    print("--- End report  ---")
    pass


if __name__ == "__main__":
    main()
