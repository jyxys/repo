

#
# 김치뽂음밥="김치볶음밥"
# pizza="pizza"
# sandwich="sandwich"
#
#
# print("Monday:" +김치뽂음밥)
# print("Tuesday:" +pizza)
# print("Wednesday:" +sandwich)
# print("목요일:" +김치뽂음밥)
# print("금요일:" +pizza)
# print("토요일:" +sandwich)
# print("일요일:" +pizza)
#
#
# word= "lets meet at =:+ at the &"
# a  =word.replace("=","3")
# b = a.replace("+","45")
# print(b.replace("&","close Taco Bell."))
#
#
# a = input("what's your name? ")
#
# print("HELLO "+ a)
#
# b=input("Are you ready?")
#
# print("For an adventure!?!")
#
#
# a = int(input("바꾸고 싶은 원를 입력하세요? :"))
#
# print("입력한 숫자의 미국 달라 기준은? ", a/1200)
# print("입력한 숫자의 유로 기준은? ", a*1340)
#
#
#
#
# a= input("Hello traveler do you care to share your name?")
#
# print(" Ohhhh, hello " + a)
#
# b=input ("Hey what is that on the ground?")
#
# print("that is a " + b)
#
# c=input("what is that a fellow traveler.......... OH NO it's not a traveler it's a zombie!!!! use that " +b)
#
# print("")
#
#
# 리스트형 변수
# a = ["아이언맨", "토르", "캡틴아메리카","HAWKEYE","Black widow","Hulk",""]
#
# b = ["서울시", "송파구", "가락동", "헬리오시티"]
#
# print(b)
# b.append("901동")
# print(b)
# del b[4]
# del b[0:3]
# print(b)
#
#
# for
#
#
# b=input("what are you doing")
# for i in range(100000):
#     print(b)
#
#
#
# character =['fjjf','fhdjkfh','fhdsdskfjsfjkdsdsjksj']
# for character in character:
#       print(character,"out")
#
#
# for i in range(1,10):
#       print("*" *4)
#       print("*" *2)
#
#
# for i in range(5):
#     a=int(input("input number? "))
#     if a >= 5 and a < 10:
#         print("a는 5보다 큽니다")
#     elif a >1 and a < 5:
#         print("a는 5보다 작다")
#     else:
#         print("a는 10 이상")
#
#
#  사용자 에게 숫자를 입력 받아서 짝수인지 홀수 인지 판정 해주는 프로그램
#
#
# a=int(input("input number?"))
# if a%2 == 0:
#     print("짝수 입니다.")
# else:
#     print("홀수 입니다.")
#
#
#
# for i in range(10):
#       if i%2 ==0:
#             print("~" *i )
#       else:
#             print("^^" *i)
#
#
# s = 0
# for i in range(101):
#     if i % 2 == 0:
#         s = s + i
# print(s)
#
#
# a = 0
# for i in range(101):
#     if i % 3 == 0:
#         a = a + i
# print(a)
#
#
# import turtle
#
#
# s = turtle.Screen()
# t: turtle = turtle.Turtle()
#
#
# t.shape("turtle")
#
#
# t.penup()
# t.setposition(-300,300)
# t.pendown()
#
# t.speed(0)
# for i in range(4):
#     t.forward(600)
#     t.right(90)
# for i in range(10):
#     t.right(90)
#     t.forward(600)
#     t.left(90)
#     t.forward(60)
#     t.left(90)
#     t.forward(600)
#     t.right(90)
#
#
#
#
#
# s.mainloop()
#
#
# t.penup()
# t.setposition(-300,300)
# t.pendown()
#
#
# 여러 나라 국기
#
#
# import time
# import turtle
#
#
#
# t = turtle.Turtle()
# s = turtle.Screen()
#
#
# t.shape("turtle")
#
#
# # create a screen
# screen = turtle.getscreen()
# # set background color of screen
# screen.bgcolor("white")
# # set tile of screen
# screen.title("USA Flag - https://www.pythoncircle.com")
# # "Yesterday is history, tomorrow is a mystery,
# # but today is a gift. That is why it is called the present.”
# # — Oogway to Po, under the peach tree, Kung Fu Panda Movie
# oogway = turtle.Turtle()
# # set the cursor/turtle speed. Higher value, faster is the turtle
# oogway.speed(100)
# oogway.penup()
# # decide the shape of cursor/turtle
# oogway.shape("turtle")
#
# # flag height to width ratio is 1:1.9
# flag_height = 250
# flag_width = 475
#
# # starting points
# # start from the first quardant, half of flag width and half of flag height
# start_x = -237
# start_y = 125
#
# # For red and white stripes (total 13 stripes in flag), each strip width will be flag_height/13 = 19.2 approx
# stripe_height = flag_height/13
# stripe_width = flag_width
#
# # length of one arm of star
# star_size = 10
#
#
# def draw_fill_rectangle(x, y, height, width, color):
#     oogway.goto(x,y)
#     oogway.pendown()
#     oogway.color(color)
#     oogway.begin_fill()
#     oogway.forward(width)
#     oogway.right(90)
#     oogway.forward(height)
#     oogway.right(90)
#     oogway.forward(width)
#     oogway.right(90)
#     oogway.forward(height)
#     oogway.right(90)
#     oogway.end_fill()
#     oogway.penup()
#
# def draw_star(x,y,color,length) :
#     oogway.goto(x,y)
#     oogway.setheading(0)
#     oogway.pendown()
#     oogway.begin_fill()
#     oogway.color(color)
#     for turn in range(0,5) :
#         oogway.forward(length)
#         oogway.right(144)
#         oogway.forward(length)
#         oogway.right(144)
#     oogway.end_fill()
#     oogway.penup()
#
#
# # this function is used to create 13 red and white stripes of flag
# def draw_stripes():
#     x = start_x
#     y = start_y
#     # we need to draw total 13 stripes, 7 red and 6 white
#     # so we first create, 6 red and 6 white stripes alternatively
#     for stripe in range(0,6):
#         for color in ["red", "white"]:
#             draw_fill_rectangle(x, y, stripe_height, stripe_width, color)
#             # decrease value of y by stripe_height
#             y = y - stripe_height
#
#     # create last red stripe
#     draw_fill_rectangle(x, y, stripe_height, stripe_width, 'red')
#     y = y - stripe_height
#
#
# # this function create navy color square
# # height = 7/13 of flag_height
# # width = 0.76 * flag_height
# # check references section for these values
# def draw_square():
#     square_height = (7/13) * flag_height
#     square_width = (0.76) * flag_height
#     draw_fill_rectangle(start_x, start_y, square_height, square_width, 'navy')
#
#
# def draw_six_stars_rows():
#     gap_between_stars = 30
#     gap_between_lines = stripe_height + 6
#     y = 112
#     # create 5 rows of stars
#     for row in range(0,5) :
#         x = -222
#         # create 6 stars in each row
#         for star in range (0,6) :
#             draw_star(x, y, 'white', star_size)
#             x = x + gap_between_stars
#         y = y - gap_between_lines
#
#
# def draw_five_stars_rows():
#     gap_between_stars = 30
#     gap_between_lines = stripe_height + 6
#     y = 100
#     # create 4 rows of stars
#     for row in range(0,4) :
#         x = -206
#         # create 5 stars in each row
#         for star in range (0,5) :
#             draw_star(x, y, 'white', star_size)
#             x = x + gap_between_stars
#         y = y - gap_between_lines
#
# # start after 5 seconds.
# time.sleep(5)
# # draw 13 stripes
# draw_stripes()
# # draw squares to hold stars
# draw_square()
# # draw 30 stars, 6 * 5
# draw_six_stars_rows()
# # draw 20 stars, 5 * 4. total 50 stars representing 50 states of USA
# draw_five_stars_rows()
# # hide the cursor/turtle
# oogway.hideturtle()
# # keep holding the screen until closed manually
# screen.mainloop()
#
#
#
#
#
#
#
#
#
#
# t.begin_fill()
# t.color("red")
# t.circle(250)
# t.end_fill()
#
#
# import turtle
# aze = turtle.Turtle()
#
# aze.shape('turtle')
#
# def makeStar():
#         for k in range(5):
#                 aze.forward(20)
#                 aze.right(144)
#
# for i in range(12):
#         makeStar()
#         aze.left(30)
#         aze.penup()
#         aze.forward(50)
#         aze.pendown()
# turtle.mainloop()
#
#
# def draw_shape(radius, color1):
#     t.left(270)
#     t.width(3)
#     t.color("black", color1)
#     t.begin_fill()
#     t.circle(radius/2.0, -180)
#     t.circle(radius,180)
#     t.left(180)
#     t.circle(-radius/2.0, -180)
#     t.end_fill()
# t = turtle.Turtle()
# t.reset()
# draw_shape(100,"red")
# t.setheading(180)
# draw_shape(100, "blue")
#
# # 태극기 긴 검은 줄
# def long():
#     t.begin_fill()
#     t.forward(100)
#     t.left(90)
#     t.forward(12.5)
#     t.left(90)
#     t.forward(100)
#     t.left(90)
#     t.forward(12.5)
#     t.end_fill()
#
# # 태극기 짧은 줄
# def short():
#     t.begin_fill()
#     t.forward(45)
#     t.left(90)
#     t.forward(12.5)
#     t.left(90)
#     t.forward(45)
#     t.left(90)
#     t.forward(12.5)
#     t.end_fill()
#
# # 태극기 간격 1
# def space1():
#     t.left(180)
#     t.penup()
#     t.forward(18.75)
#     t.pendown()
#     t.right(90)
#
# # 태극기 간격 2
# def space2():
#     t.left(90)
#     t.penup()
#     t.forward(55)
#     t.pendown()
#
# # 태극기 간격 3
# def space3():
#     t.right(90)
#     t.penup()
#     t.forward(55)
#     t.pendown()
#     t.left(180)
#
# # 태극기 간격 4
# def space4():
#     t.penup()
#     t.forward(18.75)
#     t.pendown()
#     t.left(90)
#
#
#
# t.penup()
# t.setposition(-300,140)
# space1()
#
#
#
#
# s.mainloop()


# import turtle
#
# tortoise = turtle.Turtle()
# s = turtle.Screen()
#
# tortoise.shape("turtle")
#
# tortoise.penup()
# tortoise.shapesize(3)
# tortoise.color("navy")
# tortoise.setposition(-200,0)
#
# def forward():
#     tortoise.forward(1000)
#
# def back():
#     tortoise.back(1000)
#
#
#
#
# s.onkey(back,"s")
# s.onkey(forward,"w")
# s.listen()
#
# oogway = turtle.Turtle()
#
# oogway.shape("turtle")
#
# oogway.penup()
# oogway.shapesize(3)
# oogway.color("darkred")
# oogway.setposition(200,0)
# oogway.setheading(180)
#
# oog = turtle.Turtle()
#
# oog.pensize(5)
# oog.up()
# oog.setposition(-300,300)
# oog.setheading(270)
# oog.down()
# oog.hideturtle()
#
# for w in range(3):
#     oog.forward(600)
#     oog.left(90)
#
#
# s.mainloop()






# a = "python\n"
#
# print(a*2)
#
#
# print("=" * 50)
# # print("My Program")
# print("=" * 50)
#
#
# a = "010-5802-3333"
#
# print(a[9:])
#
#
#
#
#
# a = "like"
# b = "totally"
# print(f"I {a} apples {b}.")
#
#
#
# a = "hobby"
# print(a.count('b'))
#
#
# a = "Python is simple compared to java."
# print(a.find('j'))
#
#
# print("I".join('qwerty'))
#
#
#
#
# a = "You are to short."
#
#
# print(a.replace("short", "long"))



# a = "010-222-22-444-4444"
#
# print(a.split("-"))






# import turtle
#
#
#
# bowser = turtle.Turtle()
# s = turtle.Screen()
#
# bowser.speed(1000000000000000)
# bowser.shape("turtle")
#
# bowser.penup()
# bowser.setposition(300,300)
# bowser.pendown()
# for w in range(4):
#     bowser.forward(100)
#     bowser.left(90)
# bowser.penup()
# bowser.setposition(300,-100)
# bowser.pendown()
# bowser.forward(100)
# bowser.back(50)
# bowser.left(90)
# bowser.forward(50)
# bowser.setheading(270)
# bowser.forward(100)
# bowser.penup()
# bowser.setposition(-300,-100)
# bowser.pendown()
# bowser.circle(50)
# bowser.penup()
# bowser.setposition(-300,300)
# bowser.pendown()
# bowser.right(90)
# for e in range(3):
#     bowser.right(120)
#     bowser.forward(100)
#
#
#
#
# s.mainloop()




# hit = 0
# while hit < 20:
#     hit = hit +1
#     print("You hit the tree %d times." % hit)
#     if hit == 20:
#       print("The tree fell.")

# prompt = "print"
#
# number = 0
# number = int(input(" TYPE A NUMBER"))
#
# while number == 0 or number == 5:
#     print(prompt)

# coffee = 10
# while True:
#
#     money = int(input("GIVE ME THE MONEY:"))
#     if money == 300:
#         print("ME GIVE YOU BROWN SOUR DRINK.")
#         coffee =coffee -1
#     elif money > 300:
#         print("You have %d change left." % (money -300))
#         coffee = coffee -1
#     else:
#         print("I GIVE YOU MONEY I DO NOT GIVE YOU COFFEE")
#         print("YOU HAVE %d LEFT." % coffee)
#     if coffee == 0:
#         print("ME HAVE NO COFFEE AND PROFITS, GO AWAY.")
#         break

# a= 0
# while a < 10:
#     a = a +1
#     if a%2 == 0:
#         continue
#     print(a)



# import turtle
#
#
# bowser = turtle.Turtle()
# s = turtle.Screen()
# bowser.speed(100000)
# bowser.shape("turtle")
# bowser.hideturtle()
#
# def draw():
#     for i in range(360):
#         bowser.right(i)
#         for t in range(4):
#             bowser.forward(100)
#             bowser.right(90)
#
# draw()
# # Defined and called the function
#
# s.mainloop()


# import turtle
#
#
# oogway = turtle.Turtle()
# s = turtle.Screen()
#
# oogway.shape("turtle")
# oogway.setposition(-200,0)
# def draw():
#     for t in range(4):
#         oogway.forward(100)
#         oogway.right(90)
#     oogway.setx(oogway.xcor()+ 100)
# for f in range(4):
#     draw()
# s.mainloop()




# n = int(input())
#
# for i in range(n + 1):
#     for j in range(1,i + 1):
#         print(j,end=' ')
#     print()

# n = int(input())
# for i in range(n,-1,-1):
#     print(i)



# a = input()
#
# sum = 0
# for i in range(len(a)):
#     sum += int(a[i])
# print(sum)


# a = int(input())
# b = int(input())
# c = int(input())
#
# print(a + b + c)


# a = input()
# b = input()
# c = input()
# print(c)
# print(b)
# print(a)


# n = int(input())
# for i in range(1,n + 1):
#     print("*" * i)
#     if i == 3:
#         for j in range(n - 1 ,-1,-1):
#             print("*"* j)

# a = input()
# if a.isupper():
#     print(0)
# elif a.islower():
#     print(1)

# a = int(input())
#
# if a > 0:
#     print(a * 3)
# elif a < 0:
#     print(a * 2)
# else:
#     print(0)


# def solution(k,n):
#     a = 0
#     for i in range(n):
#         a = k + 3*i
#         print(a,end=" ")
#
# solution(7,5)

# a = [14,45,50,3,7,11,5,23,9,80]
#
# def solution(n):
#     for i in range(len(n)):
#         if n[i] == 7:
#             print(i)
# solution(a)

# def solution(n1,n2):
#     if n1 > n2:
#         return n2
#     else:
#         return n1
#
# print(solution(27,64))

#
# import turtle
# import random
# import time
#
# t = turtle.Turtle()
# s = turtle.Screen()
#
# playing = 1
# while playing:
#     rand_numbers = [i for i in range(1,101)]
#     rand_com = []
#
#     while True:
#         rand_num = random.choice(rand_numbers)
#         if rand_num not in rand_com:
#             rand_com.append(rand_num)
#         if len(rand_com) == 4:
#             break
#
#     t.hideturtle()
#     for i in range(len(rand_com)):
#         t.clear()
#         t.write(rand_com[i],False,"center",font= ("",100,"bold"))
#         time.sleep(1)
#     t.clear()
#
#     print(rand_com)
#
#     answer = s.textinput("입력","숫자를 입력 ','로 구분 ")
#
#     print(answer)
#     answer = answer.split(",")
#     print(answer)
#
#     integer = []
#     for j in range(len(answer)):
#         integer.append(int(answer[j]))
#     print(integer)
#
#     if integer == rand_com:
#         t.write("정답",font= ("",100,"bold"))
#     else:
#         t.write("오답", font=("", 100, "bold"))
#     answer = s.numinput("입력","계속하려면  1 아니면 0 입력",1,0,1)
#     if answer == 1:
#         playing = 1
#     else:
#         playing = 0



# import random
#
# a = [i for i in range(1,11)]
# b = []
# count = 1
# while True:
#     count += 1
#     c = random.choice(a)
#     if c not in b:
#         b.append(c)
#     if len(b) == 9:
#         print(b)
#         break
# print(count)




# import turtle
# t = turtle.Turtle()
# s = turtle.Screen()
# t.speed(0)

# for i in range(3):
#     t.forward(150)
#     t.left(120)

# length = 150
# for i in range(3):
#     t.forward(length)
#     t.left(120)
#     length = length + 10

# length = 150
# for i in range(30):
#     t.forward(length)
#     t.left(120)
#     length = length + 10



# for x in range(2,10):
#     for y in range(1,10):
#         print(x, "X", y, "=",x*y, end="    ")
#         if y == 5 or y == 9:
#             print()


# a = int(input())
# b = int(input())
#
# for x in range(b,a + 1):
#     for y in range(1,10):
#         print(a, "X", y, "=",x*y ,"     ",a-1, "X", y, "=",x*y,"     ", a-2, "X", y, "=",x*y)


# a = int(input())
# for x in range(1,a + 1):
#     print("(", x,",",1,")","(", x,",",2,")","(", x,",",3,")","(", x,",",4,")")



# import turtle
# import random
#
#
# t = turtle.Turtle()
# s = turtle.Screen()
# t.shape("turtle")
# t.penup()
# t.setposition(-300,200)
# t.pendown()
# t.speed(0)
#
# a = -300
#
# for i in range(5):
#     t.penup()
#     t.setposition(a,200)
#     t.pendown()
#
#     a = a + 100
#
#     t.setheading(270)
#     t.forward(500)
#
#     t.penup()
#     t.setposition(-300,200)
#     t.pendown()
#
# x = [-300,-200,-100,0,100]
#
#
# t.setheading(0)
#
# for j in range(3):
#     for i in range(4):
#         b = random.randint(-200, 200)
#         print(b)
#         t.penup()
#         t.setposition(x[i],b)
#         t.pendown()
#         t.forward(100)
#
#
#
#
#
#
#
#
#
#
#
#
# s.mainloop()



# def solution(k,n):
#     a = []
#     for i in range(n):
#         a.append(k)
#         k += 3
#     return a
# for i in solution(7,5):
#     print(i , end= " ")



# def num(n1,n2):
#     if n1 < n2:
#         return n1
#     elif n2 < n1:
#         return n2
#
# print(num(27,64))


# a = list(map(int, input().split()))
# print(a)




# arr = list(map(int, input().split()))
# n = int(input("숫자 입력"))
#
# sum = 0
#
# for i in range(1, n, 2):
#     sum += arr[i]
#
# print("%d" % sum)


# n = int(input())
#
# for i in range(0,n):
#     print("_"* (i) +"*"*(n-i), end="")


# counter = 0
# str = input()
#
# for i in range(0, len(str)):
#     if str[i].islower():
#         counter += 1
# print("%d" % counter)



a = input()
b = input()

print(a + "&" + b)




qwewqeqe