current_page = 1
page_line = 1
current_line = 1
total = 0
with open('../data/search_word.txt', 'r', encoding='utf-8') as file:
    search_word = file.readline()


with open('../data/Childhood.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        if line.find(search_word) != -1:
            print(current_page)
            total += 1
        page_line += 1
        if page_line == 46:
            current_page += 1
            page_line = 1
if total == 0:
    print("There is no word!")
else:
    print("There are", total, "words in the text")
