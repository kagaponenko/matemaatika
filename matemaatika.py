from random import *
print("Matemaatika")
while True:
    try:
        r=int(input("Сложность (1, 2, 3): "))
        if 1<=r<=3:
            break
        print("Введите значение от 1 до 3")
    except ValueError:
        print("Введите правильное значение")
        
if r==1:
    q=5
    o=['+','-']
elif r==2:
    q=10
    o=['+', '-', '*', '/']
elif r==3:
    q=15
    o=['+', '-', '*', '/', '**'] 
on=len(o)
print("Будет задано",q,"вопросов с действиями",o)

ca=0
for i in range(q):
    oi=randint(0, on-1)
    op=o[oi]
    if r==1:
        a=randint(1, 10)
        b=randint(1, 10)
    elif r==2:
        a=randint(1, 15)
        b=randint(1, 15)
    elif r==3:
        a=randint(1, 20)
        b=randint(1, 20)
        
    print()
    j=i+1
    print(f"Вопрос номер {j}: ", a,op,b) 
    
    while True:
        try:
            an=float(input("Ответ: "))
            break
        except ValueError:
            print("Введите правильное значение")
            
    if op=='+':
        va=a+b
    elif op=='-':
        va=a-b
    elif op=='*':
        va=a*b
    elif op=='/':
        va=a/b
    elif op=='**':
        va=a**b

    if an==va:
        print("Правильно")
        ca+=1
    else:
        print("Неправильно. Правильный ответ:", va)   
print()
print("Количество правильных ответов: ", ca)
print()

s=(ca/q)*100
print(f"Результат: {s}%")

if s<60:
    h=2
elif 60<=s<75:
    h=3
elif 75<=s<90:
    h=4
else:
    h=5
print("Оценка",h)
