with open('../data/Childhood.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        if line.find('подарки') != -1:
            print(line.find('подарки'))
