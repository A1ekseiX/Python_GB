print('Welcome to time converter')
duration=int(input('enter a positive integer: '))
day = duration // 86400
hour = (duration - (day * 86400)) // 3600
minute = (duration - ((day * 86400) + (hour*3600))) // 60
second = duration - ((day * 86400) + (hour * 3600) + (minute * 60))

if duration <= 59:
    print(second, 's')
elif duration >= 60 and duration <= 3599:
    print(f"{minute} m: {second} s")
elif duration >= 3600 and duration <= 86399:
    print(f"{hour} h: {minute} m: {second} s")
else:
    print(f"{day} d: {hour} h: {minute} m: {second} s")
