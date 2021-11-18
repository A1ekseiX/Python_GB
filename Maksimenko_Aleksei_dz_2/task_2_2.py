sentence = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была',
            '+5', 'градусов']
print(*sentence, sep=' ')
for el in range(len(sentence)):
    if sentence[el].isdigit():
        sentence[el] = f'"{int(sentence[el]):02d}"'
    elif sentence[el].startswith("+"):
        sentence[el] = f'"{int(sentence[el]):+03d}"'
print(*sentence, sep=" ")
