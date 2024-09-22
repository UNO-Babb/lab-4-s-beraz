#TurtleGraphics.py
#Name:Skye Beraz	
#Date:9/21/2024
#Assignment:Lab 4

def main():
	def drawSquare(squint, squareSize):
		for i in range(4):
			squint.forward(squareSize)
			squint.right(90)


	def drawPolygon(squint, polySides):
		for i in range(polySides):
			squint.forward(50)
			squint.right(polyTurn)


	def fillCorner(squint, quadrantFill):
		squint.penup()
		squint.goto(-100,100)
		squint.pendown()
		for i in range(4):
			squint.forward(200)
			squint.right(90)
		squint.penup()
		squint.goto(0,0)
		squint.pendown()
		squint.setheading(0)
		if(quadrantFill == "1"):
			squint.begin_fill()
			for i in range(4):
				squint.forward(100)
				squint.left(90)
			squint.end_fill()
		elif(quadrantFill == "2"):
			squint.right(180)
			squint.begin_fill()
			for i in range(4):
				squint.forward(100)
				squint.right(90)
			squint.end_fill()
		elif(quadrantFill == "3"):
			squint.right(180)
			squint.begin_fill()
			for i in range(4):
				squint.forward(100)
				squint.left(90)
			squint.end_fill()
		elif(quadrantFill == "4"):
			squint.begin_fill()
			for i in range(4):
				squint.forward(100)
				squint.right(90)
			squint.end_fill()
		else:
			print("That's not a valid choice!") 


	def squaresInSquares(squint, numOfSquares):
		x = 40
		squint.penup()
		squint.goto(20,20)
		squint.pendown()
		for i in range(numOfSquares):
			for i in range(4):
				squint.forward(x)
				squint.right(90)
			squint.penup()
			for i in range(2):
				squint.left(90)
				squint.forward(20)
			squint.setheading(0)
			squint.pendown()
			x += 40


	import turtle
	squint = turtle.Turtle()
	squint.shape("turtle")
	print("Hello! My name is Squint, and I'm an artist. Would you like to see what I can draw?")
	print("Type the name of the art piece below. Be sure to use the same capitalization, or I won't know what you want me to draw!")
	draw = "Y"
	while(draw == "Y"):
		print("__________________________________")
		print("   ")
		print("drawSquare")
		print("drawPolygon")
		print("fillCorner")
		print("squaresInSquares")
		print("    ")
		print("__________________________________")
		art = input("What can I draw for you? ")
		squint.goto(0,0)
		squint.clear()
		squint.setheading(0)
		if(art == "drawSquare"):
			squareSize = int(input("How BIG should I draw the sides? I would suggest anywhere between 50 and 500. "))
			drawSquare(squint, squareSize)
		elif(art == "drawPolygon"):
			polySides = int(input("How many sides should I draw? Pick a number between 3-12! "))
			polyTurn = int(360/polySides)
			drawPolygon(squint, polySides)
		elif(art == "fillCorner"):
			quadrantFill = input("Okay, but only if you pick a number between 1 and 4! ")
			fillCorner(squint, quadrantFill)
		elif(art == "squaresInSquares"):
			numOfSquares = int(input("How many squares do you want me to draw? No more than 15 please... All that running makes me so sleepy. "))
			squaresInSquares(squint, numOfSquares)
		else:
			print("That's not a valid choice!")
		print("There you go! Do you like it? I hope you do.")	
		draw = input("Would you like me to draw something else for you? Y/N ")
	print("Thanks for drawing with me, I had so much fun!")


main()
