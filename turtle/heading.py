import turtle

def main():
	w = turtle.Screen()
	w.setup(600, 600)
	w.clear()
	t = turtle.Turtle()
	t.hideturtle()
	t.goto(0,0)
	
	t.seth(0)
	t.forward(100)
	t.pencolor('#FF0000')
	t.fillcolor('#FF0000')
	t.begin_fill()
	for n in range (0,4):
		t.forward(50)
		t.left(90)
	t.end_fill()
	
	t.goto(0,0)
	t.seth(90)
	t.forward(100)
	t.pencolor('#00FF00')
	t.fillcolor('#00FF00')
	t.begin_fill()
	for n in range (0,4):
		t.forward(50)
		t.left(90)
	t.end_fill()
	
	t.goto(0,0)
	t.seth(180)
	t.forward(100)
	t.pencolor('#0000FF')
	t.fillcolor('#0000FF')
	t.begin_fill()
	for n in range (0,4):
		t.forward(50)
		t.left(90)
	t.end_fill()
	
	t.goto(0,0)
	t.seth(270)
	t.forward(100)
	t.pencolor('#FFFF00')
	t.fillcolor('#FFFF00')
	t.begin_fill()
	for n in range (0,4):
		t.forward(50)
		t.left(90)
	t.end_fill()
	
	
	p = input(" hello ")
	
if __name__ == '__main__':
	main()
