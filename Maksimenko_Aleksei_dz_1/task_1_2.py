result=[]
for i in range(1,1000,2):
        result.append(i**3)

sum_result=0
for i in range(len(result)):
    sum_digits=0
    num=result[i]
    while num != 0:
        sum_digits=sum_digits + num % 10
        num=num // 10
    if sum_digits %7==0:
        sum_result+=result[i]
print("The sum of those numbers from this list, the sum of the digits of which is divisible by 7:", sum_result)

sum_result_17=0
for i in range(len(result)):
    sum_digits=0
    num=result[i]+17
    while num!=0:
        sum_digits=sum_digits+num % 10
        num= num //10
    if sum_digits %7 ==0:
        sum_result_17+=result[i]+17
print("The sum after recalculation:", sum_result_17)
