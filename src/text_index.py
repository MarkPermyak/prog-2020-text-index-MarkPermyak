current_page = 1
page_line = 1
current_line = 1

number_of_word = 0

list_of_words = list()
total = list()

with open('../data/search_words.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        list_of_words.append(line.strip())
        total.append(0)


with open('../data/Childhood.txt', 'r', encoding='utf-8') as file:
    for search_word in list_of_words:
        print("Word "+"'"+search_word+"'"+":")
        for line in file.readlines():
            if line.find(search_word) != -1:
                print(current_page)
                print(line)
                total[number_of_word] += 1
            page_line += 1
            if page_line == 46:
                current_page += 1
                page_line = 1

        current_page = current_line = page_line = 1
        file.seek(0)
        number_of_word += 1


totals_and_words = dict()
for j in range(len(total)):
    totals_and_words[total[j]] = list_of_words[j]


total.sort()
total.reverse()

for i in range(len(total)):
    if total[i] == 0:
        print("There is no word", "'" + totals_and_words[i] + "'", "in the text")
    else:
        if total[i] == 1:
            print("There is", total[i], "word", "'" + totals_and_words[total[i]] + "'", "in the text")
        else:
            print("There are", total[i], "words", "'" + totals_and_words[total[i]] + "'", "in the text")
