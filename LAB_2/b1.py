print("Pavel Puzach")
print("Simple Map Distance Computations")
print()

with open(r"C:\Users\grodn\pasha\Univer\university-1st-year-fse-\LAB_2\inmap3.dat", "r") as file:
    content = file.read()
    
    numbers = [float(x) for x in content.split()]


print('Map Scale Factor: ', numbers[1], ' miles per inch')
print()
print('          Map         Mileage')
print('          Measure     Distance')

print('=' * 100)

count = int(numbers[0])

summa = []

for i in range(count):
    row_num = i + 1
    znachenie = numbers[i + 2]
    itog = round(znachenie * numbers[1] + 0.00001,1)
    #itog = znachenie * numbers[1]
    print('#  ',row_num,'     ',znachenie,'       ',itog)
    summa.append(itog)

print('=' * 100)

total = sum(summa)

print("Total Distance:      ", total)
