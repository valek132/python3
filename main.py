"""def sum_odd_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Сумма равна: {s}")
lst = []
lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_index(lst)
"""



"""mass = [2, 3, 4, 5, 6]
mass2=[]
for i in range(len(mass)//2+len(mass)%2):
    mass2.append(mass[i]*mass[len(mass)-1-i])
print(mass2)"""




"""lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(max(new_lst) - min(new_lst))"""




"""s = ""
n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
while n != 0:
    s = str(n%2) + s
    n //=2
print(s)"""



n = int(input('Введите число: '))

def get_fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n-1):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

fibo_nums = get_fibonacci(n+1)
print(fibo_nums)