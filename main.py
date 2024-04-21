
def sort_on(dict):
    return dict["count"]

def count_letters(text):
    lower_case_text = text.lower()
    count = {}
    for c in lower_case_text:
        if not c.isalpha():
            continue
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    return count


def convert_dict(count_dict):
    list_of_dict = []
    for l in count_dict:
        list_of_dict.append({"letter": l, "count": count_dict[l]})
    return list_of_dict


def count_words(text):
    return len(text.split())


def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
        print(f"--- Begin report of {file_path} ---")
        print(f"{count_words(file_contents)} words found in the document\n")
        count = convert_dict(count_letters(file_contents))
        count.sort(reverse=True, key=sort_on)
        for c in count:
            print(f"The '{c['letter']}' character was found '{c['count']}' times")
        print("--- End report ---")


main()
