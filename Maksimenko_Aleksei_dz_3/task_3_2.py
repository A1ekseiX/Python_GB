def thesaurus(*args):
    my_dictionary = dict()
    for name in args:
        i = name[0]
        if i not in my_dictionary:
            my_dictionary[i] = []
        my_dictionary[i].append(name)
    return my_dictionary


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
