from gfxhat import lcd,backlight


backlight.set_all(255, 0, 0)
backlight.show()

lcd.clear()
lcd.show()

#lists
pm = [[0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]


#get user input for x and y 1
x=0
y=0

for row in pm:
	y= y + 1

	for state in row:
		x = x + 1

		lcd.set_pixel(x, y, state)
	x=0
lcd.show()


backlight.set_all(255, 0, 0)
backlight.show()

lcd.clear()
lcd.show()


f1 =  [
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[1,0,1,1,1,1,0,1],
[1,0,0,1,1,0,0,1],
[1,0,0,1,1,0,0,1],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0]
]


x=0
y=0

for row in f1:
	y= y + 1

	for state in row:
		x = x + 1

		lcd.set_pixel(x, y, state)
	x=0
lcd.show()

backlight.set_all(255, 0, 0)
backlight.show()

lcd.clear()
lcd.show()

