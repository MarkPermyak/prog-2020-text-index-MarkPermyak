list_of_words = list()
total = list()

current_page = 1
page_line = 1
number_of_word = 0
with open('../data/search_words.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        list_of_words.append(line.strip())
        # решить вопрос с лес и лестница
        total.append(0)

result_file = open('../src/result.txt', 'w', encoding='utf-8')


def find_a_word(word_to_find, initial_file, with_pages, with_lines):
    current_page0 = 1
    page_line0 = 1
    number_of_word0 = 0
    for line0 in initial_file.readlines():
        if line0.find(word_to_find) != -1:
            if with_pages == 1:
                result_file.write(str(current_page0))
                result_file.write('\n')
            if with_lines == 1:
                result_file.write(line0)
                result_file.write('\n')
            total[number_of_word0] += 1
        page_line0 += 1
        if page_line0 == 46:
            current_page0 += 1
            page_line0 = 1
    initial_file.seek(0)
    number_of_word0 += 1


def text_index():
    with open('../data/Childhood.txt', 'r', encoding='utf-8') as file0:
        for search_word in list_of_words:
            result_file.write("Word "+"'"+search_word+"'"+":"+'\n')
            find_a_word(search_word, file0, 1, 0)
            result_file.write('\n')


def print_lines():
    with open('../data/Childhood.txt', 'r', encoding='utf-8') as file0:
        for search_word in list_of_words:
            result_file.write("Word "+"'"+search_word+"'"+":"+'\n')
            find_a_word(search_word, file0, 0, 1)
            result_file.write('\n')


text_index()
print_lines()


result_file.close()
