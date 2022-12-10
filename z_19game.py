from turtle import*


print('Привет. Добро пожаловать в игру!\
\n Здесь ты сможешь выбрать себе автомобиль для гонок.\
\nСледуй указаниям и составь себе свой гоночный автомобиль!\
\nПримечание: ответы на вопросы пиши как написано в самих вопросах\
\n(букву ё пиши как е. Все слова пиши с маленькой буквы)\
\n         \
\nВ этой программе я использовал и работал с модулем turtle.\
\n           \
\n           ')



b=input('Для начала выбери цвет автомобиля из предложенных\
	\n (красный,синий,зеленый,желтый): ')

if b == 'красный':
	color= 'red'

elif b == 'синий':
	color= 'blue'

elif b == 'зеленый':
	color= 'green'

elif b == 'желтый':
	color= 'yellow'















a=input('Теперь выберем какой тип тебе подходит.\
	\nВыбери из предложенных(грузовик, легковушка): ')

if a=='грузовик':
	
	с = input('Отлично! Хотите ли вы добавить турбоускоритель? Напишите либо да либо нет: ')
	if с == 'нет':

		pu()
		rt(180)
		fd(200)
		rt(180)
		fd(400)
		lt(90)
		pd()

		fillcolor(color)
		begin_fill()


		fd(200)
		lt(90)
		fd(300)
		lt(90)
		fd(200)
		lt(90)
		fd(300)
		lt(90)

		end_fill()

		fd(200)
		lt(90)
		fd(300)
		lt(90)
		fd(45)
		rt(90)

		fillcolor(color)
		begin_fill()

		fd(90)
		lt(60)
		fd(30)
		lt(30)
		fd(130)
		lt(90)
		fd(105)
		lt(90)
		fd(150)

		end_fill()

		rt(180)
		fd(10)
		rt(90)
		pu()
		fd(20)
		pd()
		fillcolor('white')
		begin_fill()

		for x in range(4):
			fd(40)
			lt(90)

		end_fill()

		pu()
		rt(180)
		fd(10)
		rt(90)
		fd(110)
		rt(90)
		fd(20)
		pd()


		fillcolor('black')
		begin_fill()
		#колеса
		for x in range(360//2):
			fd(1)
			lt(2)
		end_fill()

		pu()	
		rt(180)
		fd(250)
		pd()

		fillcolor('black')
		begin_fill()
		for x in range(360//2):
			fd(1)
			rt(2)
		end_fill()











	elif с == 'да':
		
		pu()
		rt(180)
		fd(200)
		rt(180)
		fd(400)
		lt(90)
		pd()

		fillcolor('red')
		begin_fill()


		fd(200)
		lt(90)
		fd(300)
		lt(90)
		fd(200)
		lt(90)
		fd(300)
		lt(90)

		end_fill()

		fd(200)
		lt(90)
		fd(300)
		lt(90)
		fd(45)
		rt(90)

		fillcolor('red')
		begin_fill()

		fd(90)
		lt(60)
		fd(30)
		lt(30)
		fd(130)
		lt(90)
		fd(105)
		lt(90)
		fd(150)

		end_fill()

		rt(180)
		fd(10)
		rt(90)
		pu()
		fd(20)
		pd()
		fillcolor('white')
		begin_fill()

		for x in range(4):
			fd(40)
			lt(90)

		end_fill()

		pu()
		rt(180)
		fd(10)
		rt(90)
		fd(110)
		rt(90)
		fd(20)
		pd()


		fillcolor('black')
		begin_fill()
		#колеса
		for x in range(360//2):
			fd(1)
			lt(2)
		end_fill()

		pu()	
		rt(180)
		fd(250)
		pd()

		fillcolor('black')
		begin_fill()
		for x in range(360//2):
			fd(1)
			rt(2)
		end_fill()



		pu()
		lt(90)
		fd(170)
		lt(90)
		fd(50)
		rt(180)
		pd()


		fillcolor('black')
		begin_fill()
		fd(60)
		lt(90)
		fd(48)
		lt(90)
		fd(60)
		lt(90)
		fd(48)
		lt(90)
		end_fill()


		fillcolor('black')
		begin_fill()
		fd(60)
		lt(30)
		fd(40)
		lt(60)
		fd(10)
		lt(65)
		fd(40)
		end_fill()

		pu()
		fd(300)
		pd()

























elif a=='легковушка':

	c = input('Отлично! Хотите ли вы добавить спойлер к машине? Напишите либо да либо нет: ')
	if c == 'нет':

		pu()
		rt(180)
		fd(200)
		rt(180)
		fd(400)
		lt(30)
		pd()

		fillcolor(color)
		begin_fill()

		fd(20)
		lt(30)
		fd(20)
		lt(30)
		fd(20)
		lt(30)
		fd(20)
		lt(55)

		fd(40)
		rt(50)
		fd(50)
		lt(55)
		fd(150)
		lt(40)
		fd(90)
		rt(40)
		fd(100)
		lt(45)
		fd(72)

		rt(225)
		fd(420)

		end_fill()

		pu()
		rt(180)
		fd(20)
		rt(90)
		fd(12)

		#колеса

		fillcolor('black')
		begin_fill()
		for x in range(360//2):
			fd(1)
			lt(2)
		end_fill()



		pu()
		lt(90)
		fd(235)
		rt(90)

		fillcolor('black')
		begin_fill()
		for x in range(360//2):
			fd(1)
			lt(2)
		end_fill()


		#стекла

		pu()
		fd(45)
		rt(90)
		fd(10)
		pd()



		fillcolor('white')
		begin_fill()


		lt(45)
		fd(55)
		rt(45)
		fd(45)
		rt(90)
		fd(40)
		rt(90)
		fd(85)

		end_fill()













	elif c == 'да':

		pu()
		rt(180)
		fd(200)
		rt(180)
		fd(400)
		lt(30)
		pd()

		fillcolor(color)
		begin_fill()

		fd(20)
		lt(30)
		fd(20)
		lt(30)
		fd(20)
		lt(30)
		fd(20)
		lt(55)

		fd(40)
		rt(50)
		fd(50)
		lt(55)
		fd(150)
		lt(40)
		fd(90)
		rt(40)
		fd(100)
		lt(45)
		fd(72)

		rt(225)
		fd(420)

		end_fill()

		pu()
		rt(180)
		fd(20)
		rt(90)
		fd(12)

		#колеса

		fillcolor('black')
		begin_fill()
		for x in range(360//2):
			fd(1)
			lt(2)
		end_fill()



		pu()
		lt(90)
		fd(235)
		rt(90)

		fillcolor('black')
		begin_fill()
		for x in range(360//2):
			fd(1)
			lt(2)
		end_fill()


		#стекла

		pu()
		fd(45)
		rt(90)
		fd(10)
		pd()



		fillcolor('white')
		begin_fill()


		lt(45)
		fd(55)
		rt(45)
		fd(45)
		rt(90)
		fd(40)
		rt(90)
		fd(85)

		end_fill()


		pu()
		rt(180)
		fd(245)
		lt(90)
		fd(10)
		pd()


		pensize(3)

		rt(40)
		fd(60)
		rt(50)
		fd(10)
		rt(180)
		fd(20)


		pu()
		fd(500)
		pd()


input('')











