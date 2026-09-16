num = int(input())

res = "Even" if (num % 2) == 0 else "Odd"

print(res)



x = int(input())

y = int(input())

z = int(input())



res = 'x' if (x > y and x > z) else ('y' if y > z else 'z')

print(f"Greatest among {x},{y},{z} is {res}")

#largest = a if a > b and a > c else b if b > c else c