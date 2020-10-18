current_page = 1
page_line = 1
current_line = 1
total = 0
number_of_words = 0


list_of_words = list()

with open('../data/search_words.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        list_of_words.append(line.strip())


with open('../data/Childhood.txt', 'r', encoding='utf-8') as file:
    for search_word in list_of_words:
        for line in file.readlines():
            if line.find(search_word) != -1:
                print(current_page)
                print(line)
                total += 1
            page_line += 1
            if page_line == 46:
                current_page += 1
                page_line = 1
        if total == 0:
            print("There is no word", "'" + search_word + "'","in the text")
        else:
            print("There are", total, "words", "'" + search_word + "'", "in the text")
        current_page = current_line = page_line = 1
        total = 0
        file.seek(0)
