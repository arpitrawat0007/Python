# # import turtle

# # window = turtle.Screen()
# # window.bgcolor('black')
# # window.title("Galactic Flower made by Arpit Rawat")

# # galatic = turtle.Turtle()
# # galatic.speed(20)
# # galatic.color('white')

# # rotate=int(180)

# # def Circles(t,size):
# #     for i in range(10):
# #         t.circle(size)
# #         size=size-4

# # def drawCircles(t,size,repeat):
# #   for i in range (repeat):
# #     Circles(t,size)
# #     t.right(360/repeat)

# # drawCircles(galatic,150,10)

# # t1 = turtle.Turtle()
# # t1.speed(20)
# # t1.color('red')

# # rotate=int(90)

# # def Circles(t,size):
# #     for i in range(4):
# #         t.circle(size)
# #         size=size-10

# # def drawCircles(t,size,repeat):
# #     for i in range (repeat):
# #         Circles(t,size)
# #         t.right(360/repeat)
# # drawCircles(t1,130,10)
# # t2= turtle.Turtle()
# # t2.speed(20)
# # t2.color('blue')

# # rotate=int(80)

# # def Circles(t,size):
# #     for i in range(4):
# #         t.circle(size)
# #         size=size-5

# # def drawCircles(t,size,repeat):
# #     for i in range (repeat):
# #         Circles(t,size)
# #         t.right(360/repeat)

# # drawCircles(t2,110,10)
# # t3 = turtle.Turtle()
# # t3.speed(20)
# # t3.color('orange')

# # rotate=int(90)

# # def Circles(t,size):
# #     for i in range(4):
# #         t.circle(size)
# #         size=size-19

# # def drawCircles(t,size,repeat):
# #     for i in range (repeat):
# #         Circles(t,size)
# #         t.right(360/repeat)

# # drawCircles(t3,80,10)
# # t4= turtle.Turtle()
# # t4.speed(20)
# # t4.color('green')

# # rotate=int(90)

# # def Circles(t,size):
# #     for i in range(4):
# #         t.circle(size)
# #         size=size-20

# # def drawCircles(t,size,repeat):
# #     for i in range (repeat):
# #         Circles(t,size)
# #         t.right(360/repeat)

# # drawCircles(t4,40,10)

# # turtle.done()















# from turtle import *
# import random

# speed(speed ='fastest')

# def draw(n, x, angle):
# 	# loop for number of stars
# 	for i in range(n):
		
# 		colormode(255)
		
# 		# choosing random integers
# 		# between 0 and 255
# 		# to generate random rgb values
# 		a = random.randint(0, 255)
# 		b = random.randint(0, 255)
# 		c = random.randint(0, 255)
		
# 		# setting the outline
# 		# and fill colour
# 		pencolor(a, b, c)
# 		fillcolor(a, b, c)
		
# 		# begins filling the star
# 		begin_fill()
		
# 		# loop for drawing each star
# 		for j in range(5):
			
# 			forward(5 * n-5 * i)
# 			right(x)
# 			forward(5 * n-5 * i)
# 			right(72 - x)
			
# 		# colour filling complete
# 		end_fill()
		
# 		# rotating for
# 		# the next star
# 		rt(angle)
# # setting the parameters
# n = 30 # number of stars
# x = 144 # exterior angle of each star
# angle = 12 # angle of rotation for the spiral

# draw(n, x, angle)

# turtle.done()














# import turtle

# # initialising variables
# dist = 1
# flag = 500

# # initialising turtle
# spiral = turtle.Turtle()

# # changing speed of turtle
# spiral.speed(10)

# # making pattern
# while flag:

# 	# makes the turtle to move forward
# 	spiral.forward(dist)
	
# 	# makes the turtle to move left
# 	spiral.left(120)
# 	spiral.left(1)
# 	dist += 1
# 	flag -= 1

# turtle.done()


# sum = 0
# while (True):
# 	userInput = input("Enter the item price or press q to quit: \n")
# 	if (userInput!='q'):
# 		sum = sum + int(userInput)
# 		print(f"Order total so far: {sum}")
# 	else:
# 		print(f"Your Bill total is {sum}. Thanks for shopping with us")
# 		break




import turtle
turtle.setup(width=600, height=500)
turtle.reset()
turtle.hideturtle()
turtle.speed(0)

turtle.bgcolor('black')

c = 0
x = 0

colors = [
#reddish colors
(1.00, 0.00, 0.00),(1.00, 0.03, 0.00),(1.00, 0.05, 0.00),(1.00, 0.07, 0.00),(1.00, 0.10, 0.00),(1.00, 0.12, 0.00),(1.00, 0.15, 0.00),(1.00, 0.17, 0.00),(1.00, 0.20, 0.00),(1.00, 0.23, 0.00),(1.00, 0.25, 0.00),(1.00, 0.28, 0.00),(1.00, 0.30, 0.00),(1.00, 0.33, 0.00),(1.00, 0.35, 0.00),(1.00, 0.38, 0.00),(1.00, 0.40, 0.00),(1.00, 0.42, 0.00),(1.00, 0.45, 0.00),(1.00, 0.47, 0.00),
#orangey colors
(1.00, 0.50, 0.00),(1.00, 0.53, 0.00),(1.00, 0.55, 0.00),(1.00, 0.57, 0.00),(1.00, 0.60, 0.00),(1.00, 0.62, 0.00),(1.00, 0.65, 0.00),(1.00, 0.68, 0.00),(1.00, 0.70, 0.00),(1.00, 0.72, 0.00),(1.00, 0.75, 0.00),(1.00, 0.78, 0.00),(1.00, 0.80, 0.00),(1.00, 0.82, 0.00),(1.00, 0.85, 0.00),(1.00, 0.88, 0.00),(1.00, 0.90, 0.00),(1.00, 0.93, 0.00),(1.00, 0.95, 0.00),(1.00, 0.97, 0.00),
#yellowy colors
(1.00, 1.00, 0.00),(0.95, 1.00, 0.00),(0.90, 1.00, 0.00),(0.85, 1.00, 0.00),(0.80, 1.00, 0.00),(0.75, 1.00, 0.00),(0.70, 1.00, 0.00),(0.65, 1.00, 0.00),(0.60, 1.00, 0.00),(0.55, 1.00, 0.00),(0.50, 1.00, 0.00),(0.45, 1.00, 0.00),(0.40, 1.00, 0.00),(0.35, 1.00, 0.00),(0.30, 1.00, 0.00),(0.25, 1.00, 0.00),(0.20, 1.00, 0.00),(0.15, 1.00, 0.00),(0.10, 1.00, 0.00),(0.05, 1.00, 0.00),
#greenish colors
(0.00, 1.00, 0.00),(0.00, 0.95, 0.05),(0.00, 0.90, 0.10),(0.00, 0.85, 0.15),(0.00, 0.80, 0.20),(0.00, 0.75, 0.25),(0.00, 0.70, 0.30),(0.00, 0.65, 0.35),(0.00, 0.60, 0.40),(0.00, 0.55, 0.45),(0.00, 0.50, 0.50),(0.00, 0.45, 0.55),(0.00, 0.40, 0.60),(0.00, 0.35, 0.65),(0.00, 0.30, 0.70),(0.00, 0.25, 0.75),(0.00, 0.20, 0.80),(0.00, 0.15, 0.85),(0.00, 0.10, 0.90),(0.00, 0.05, 0.95),
#blueish colors
(0.00, 0.00, 1.00),(0.05, 0.00, 1.00),(0.10, 0.00, 1.00),(0.15, 0.00, 1.00),(0.20, 0.00, 1.00),(0.25, 0.00, 1.00),(0.30, 0.00, 1.00),(0.35, 0.00, 1.00),(0.40, 0.00, 1.00),(0.45, 0.00, 1.00),(0.50, 0.00, 1.00),(0.55, 0.00, 1.00),(0.60, 0.00, 1.00),(0.65, 0.00, 1.00),(0.70, 0.00, 1.00),(0.75, 0.00, 1.00),(0.80, 0.00, 1.00),(0.85, 0.00, 1.00),(0.90, 0.00, 1.00),(0.95, 0.00, 1.00)
]

while x < 1000:
    idx = int(c)
    color = colors[idx]
    turtle.color(color)
    turtle.forward(x)
    turtle.right(98)
    x = x + 1
    c = c + 0.1

turtle.exitonclick()





# import time

# score=int()
# print("Welcome to the General knowledge Quesions Quiz")
# time.sleep(2)
# print("Question 1")
# time.sleep(2)
# Question1 = input ("A vehicle with the national registration code ‘PK’ would originate from which country? ")
# if Question1 == ("Pakistan") or Question1 == ("pakistan"):
#     print("Correct answer")
#     score = score + 1 
# else:
#     print("Incorrect answer, the correct answer is Pakistan")
# time.sleep(2)
# print("Question 2")
# time.sleep(2)
# Question2 = input("In which English county is Blenheim Palace? ")
# if Question2 == ("Oxfordshire") or Question2 == ("oxfordshire"):
#     print("Correct answer")
#     score = score + 1
# else:
#     print("Incorrect answer, the correct answer is Oxfordshire")
# time.sleep(2)
# print("Question 3")
# time.sleep(2)
# Question3 = input("How many hours are there in a leap year? ")
# if Question3 == ("8784"):
#     print("Correct answer")
#     score = score + 1
# else:
#     print("Incorrect answer, the correct answer is 8784")
# time.sleep(2)
# print("Question 4")
# time.sleep(2)
# Question4 = input("In which sport could you win the Davis Cup? ")
# if Question4 == ("Tennis") or Question4 == ("tennis"):
#     print("Correct answer")
#     score = score + 1
# else:
#     print("Incorrect answer, the correct answer is Tennis")
# time.sleep(2)
# print("Question 5")
# time.sleep(2)
# Question5 = input("What is the capital of Afghanistan? ")
# if Question5 == ("Kabul") or Question5 == ("kabul"):
#     print("Correct answer")
#     score = score + 1
# else:
#     print("Incorrect answer, the correct answer is Kabul")
# time.sleep(2)
# print("Question 6")
# time.sleep(2)
# Question6 = input("How many golden stars feature on the flag of the European Union? ")
# if Question6 == ("twelve") or Question6 == ("Twelve") or Question6 == ("12"):
#     print("Correct answer")
#     score = score + 1
# else:
#     print("Incorrect answer, the correct answer is twelve")
# time.sleep(2)
# print("Question 7")
# time.sleep(2)
# Question7 = input("In which year did Channel 4 begin transmission in the UK? ")
# if Question7 == ("1982"):
#     print("Correct answer")
#     score = score + 1
# else:
#     print("Incorrect answer, the correct answer is 1982")
# time.sleep(2)
# print("Question 8")
# time.sleep(2)
# Question8=input("In which year did Theresa May become Prime Minister? ")
# if Question8 == ("2016"):
#     print("Correct answer")
#     score = score + 1
# else:
#     print("Incorrect answer, the correct answer is 2016")
# time.sleep(2)
# print("Question 9")
# time.sleep(2)
# Question9 = input("What is six-fourteenths of 112? ")
# if Question9 == ("48") or Question9  == ("forty eight"):
#     print("Correct answer")
#     score = score + 1
# else:
#     print("Incorrect asnwer, the correct answer is 48")
# time.sleep(2)
# print("Question 10")
# time.sleep(2)
# Question10 = input("Which type of angle is greater than 90 degrees but less than 180 degrees? ")
# if Question10 == ("obtuse") or ("Obtuse"):
#     print("Correct answer")
#     score = score + 1
# time.sleep(2)
# print("Question 11")
# time.sleep(2)
# Question11 = input("Which keyword is used for function in Python language?")
# if Question11 == ("def") or ("define"):
#     print("Correct answer")
#     score = score + 1
# time.sleep(2)
# print("This is the end of the quiz")
# time.sleep(1)
# print("You got",(score),"/ 11")
# num1 = (score)
# num2 = 11
# print('{0:.2f}%'.format((num1 / num2 * 100)))



