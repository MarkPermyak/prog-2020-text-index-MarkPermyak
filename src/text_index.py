list_of_words = list()
# список всех искомых слов
total = list()
# список, в скольких строчках встечалось в тексте каждое слово

current_page = 1
page_line = 1
number_of_word = 0
with open('../data/search_words.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        list_of_words.append(line.strip())
        # решить вопрос с лес и лестница
        total.append(0)
# заполнили список слов, список количеств пока везде 0
result_file = open('../src/result.txt', 'w', encoding='utf-8')


def find_a_word(word_to_find, initial_file, with_pages, with_lines):
    current_page0 = 1
    page_line0 = 1
    number_of_word0 = 0
    for line0 in initial_file.readlines():
        # для каждой строки в тексте
        if line0.find(word_to_find) != -1:
            if with_pages == 1:
                # если нужно вывести номера страниц
                result_file.write(str(current_page0))
                result_file.write('\n')
            if with_lines == 1:
                # если нужно вывести сами строки
                result_file.write(line0)
                result_file.write('\n')
            total[number_of_word0] += 1
            # слово встретилось, увеличиваем количество
        page_line0 += 1
        if page_line0 == 46:
            # переход на новую страницу
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
