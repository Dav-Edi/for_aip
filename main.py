def first(password: str, confirm: str):
	if (password == confirm) and len(password) >= 6: 
		print("Пароль принят")
	else:
		print("Пароль не принят")

print('task 1')
first(input('Enter password: '), input('Confirm password: '))

def second(place: int):
	if place <= 36:
		print(['Верхнее купе', 'Нижнее купе'][place%2])
	else:
		print(['Верхняя боковая', 'Нижняя боковая'][place%2])

print('task 2')
second(int(input('Enter your place: ')))

def third(year: int):
	if year % 4 == 0 and year % 100 != 0:
		print(f'Год {year} - високосный')
	else:
		print(f'Год {year} - не високосный')

print('task 3')
third(int(input('Enter year: ')))

def fourth(clr1: str, clr2: str):
	clrs = ['красный', 'синий', 'желтый']
	if clr1 not in clrs or clr2 not in clrs:
		print('ошибка')
		return
	if clr1 == 'красный' and clr2 == 'желтый':
		print('если смешать красный и желтый, то получится оранжевый')
	elif clr1 == 'синий' and clr2 == 'желтый':
		print('если смешать синий и желтый, то получится зеленый')
	else:
		print('если смешать красный и синий, то получится фиолетовый')

print('task 4')
fourth(input('Enter color 1: '), input('Enter color 2: '))

def fifth(N: int):
	stroka = ''
	words = [input() for _ in range(N)]
	for word in words:
		stroka += word + ' '
	print(stroka)

print('task 5')
fifth(int(input("Enter N: ")))

