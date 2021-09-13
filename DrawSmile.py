import turtle

#Kích thước bút
turtle.pensize(5) 
 
#Màu bút
turtle.pencolor("Red")

#Mặt tròn bên ngoài
facesize = 200
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.circle(facesize)

#Mắt
#Màu nền mắt là màu đỏ
turtle.fillcolor ("red")
turtle.penup()
turtle.goto(-100,50)
turtle.pendown()
 
# khai bao bien eyesize lưu kích thước mắt
eye_size = 17.5
 
turtle.begin_fill()
turtle.circle(eye_size)
turtle.end_fill()
turtle.penup()
 
turtle.goto(100,50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(eye_size)
turtle.end_fill()

#Mũi
turtle.penup ()
turtle.goto(0,50)
turtle.pendown()
turtle.circle(-70, steps=3)

#Miệng
turtle.penup()
turtle.goto(-100, -70)
turtle.pendown()
turtle.right(90)
turtle.circle(100,180)
turtle.mainloop()

turtle.done()