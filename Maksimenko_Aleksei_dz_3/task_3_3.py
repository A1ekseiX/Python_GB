import random


def get_jokes(i):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    sentence = []
    for i in range(i):
        sentence.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    return sentence


count = int(input('Количество шуток: '))
print(f'{get_jokes(count)}')
