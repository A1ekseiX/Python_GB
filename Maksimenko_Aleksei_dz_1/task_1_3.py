print('Склонение слова "процент":')
for i in range(100):
    my_str=str(i+1)
    my_list=list(my_str)
    if int(my_list[-1]) == 1 and i + 1 != 11:
        print('{} процент'.format(i + 1))
    elif int(my_list[-1]) > 1 and int(my_list[-1]) <= 4:
        if  i + 1 > 10 and i + 1 <= 14:
            print('{} процентов'.format(i + 1))
        else:
            print('{} процента'.format(i + 1))
    else:
        print('{} процентов'.format(i + 1))
