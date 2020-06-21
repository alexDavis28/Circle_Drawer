import turtle
import random
import time

start_time = time.time()

circlepoints = []


def setup():
    turtle.speed(0)

    turtle.penup()
    drawpoint()


def drawpoint():
    turtle.pensize(5)
    turtle.pendown()
    turtle.fd(1)
    turtle.penup()
    turtle.bk(1)
    turtle.pensize(1)


def drawcircle(points):
    for i in range(int(points)):
        drawpoint()
        circlepoints.append((turtle.xcor(), turtle.ycor()))
        turtle.rt(360 / points)
        turtle.fd(2200 / points)


def drawtimestable(points, timestable):
    for i in range(int(points)):
        turtle.penup()
        turtle.goto(circlepoints[i][0], circlepoints[i][1])
        turtle.pendown()
        circlepoint = round(((i * timestable) % points))
        turtle.goto(circlepoints[int(circlepoint)][0], circlepoints[int(circlepoint)][1])


def main():
    setup()

    # print("How many points do you want to have in your circle? (3 - 3000)")
    # points = float(input())
    points = 1000
    drawcircle(points)

    turtle.pencolor(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
    turtle.fillcolor(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))

    # print("What times table do you want to draw?")
    # timestable = float(input())
    timestable = 23
    drawtimestable(points, timestable)
    print(time.time() - start_time)
    turtle.done


main()