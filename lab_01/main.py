def f1():
    num = int(input())

    for i in range(1,num+1):
        if(i%2 == 0):
            print(f"{i}")

def f2():
    str = input()
    count = 0

    for c in str:
        if(c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
            count += 1

    print(f"Qtd de vogais: {count}")

def f3():
    numbers = []
    for i in range(5):
        numbers.append(int(input()))
    
    for i in range(1, len(numbers)):
        num = numbers[i]
        j = i - 1

        while j >= 0 and num < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
            
        numbers[j + 1] = num

    print(numbers)

def f4():
    num = input()
    sum = 0

    for c in num:
        n = int(c)
        sum += n

    print(sum)


def f5():
    num = int(input())

    print(f"--- Tabuada de {num} ---") 
    for i in range(1, 11):
        result = num * i
        print(f"        {num} x {i} = {result}")

def f6():
    min = max = 0
    for i in range(10):
        num = int(input())
        if(num < min): min = num
        if(num > max): max = num
        
f6()