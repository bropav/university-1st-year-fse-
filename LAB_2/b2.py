import os

time = []
WCtemp = []
WCeffect = []


#Открываем файл для чтения
with open(r'C:\Users\grodn\pasha\Univer\university-1st-year-fse-\LAB_2\1.WCData.txt', 'r', encoding='utf-8') as file: lines = file.readlines()

# Пропускаем первые две строки (заголовки и разделительную линию из дефисов)
for line in lines[2:]:
    line = line.strip()
    if not line:
        continue  # Пропускаем пустые строки, если они есть
        
    # Разделяем строку по пробелам (метод split() автоматически группирует несколько пробелов)
    parts = line.split()
    
    # Проверяем, что в строке есть все три колонки
    if len(parts) == 3:
        time_val = parts[0]
        air_temp = int(parts[1])  # Конвертируем температуру в число
        wind_speed = int(parts[2]) # Конвертируем скорость ветра в число

        #расчет формулой
        otvet = 35.74 + (0.6125 * air_temp) + ((0.4275 * air_temp) - 35.75) * (wind_speed ** 0.16)

        otvet_end = round(otvet, 1)

        raznica = otvet_end - air_temp

        raznica_end = round(raznica, 1)
        
        time.append(
            time_val,
        )

        WCtemp.append(
            otvet_end
        )

        WCeffect.append(
            raznica_end
        )

kolichestvo = len(WCtemp)

summa = sum(WCtemp)

midle = summa / kolichestvo

end_otvet = round(midle, 1)

number = 0
#Пример вывода получившихся данных
with open('output.txt', 'w', encoding = 'utf-8') as file:
    file.write(f"Time               Air Temap       Wind Speed\n")
    file.write(f'-'*100)
    file.write(f'\n')
    for row in time: 
        line = f"{time[number]}          {WCtemp[number]}          {WCeffect[number]}\n"
        number += 1
        file.write(line)
    file.write(f'-'*100)
    file.write(f'\n')
    file.write(f'The everage adjusted temperature, based on {kolichestvo} observations, was {end_otvet}\n')


os.system("start output.txt")