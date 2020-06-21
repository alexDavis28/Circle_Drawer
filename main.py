import turtle
import random
import time
start_time = time.time()
import math
import random

circle_points = []


def draw_point(x,y):
    # This actions as the function for the turtle to draw a single point
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot()
    turtle.penup()


def find_coord_of_point(radius, angle_degrees):
    # Assuming origin of (0,0)
    # Returns x,y
    angle = math.radians(angle_degrees)
    x = radius*math.cos(angle)
    y = radius*math.sin(angle)
    return x, y


def main():
    # Set up the turtle
    turtle.speed(0)

    points = 0.0
    while (points < 1) or (points > 3000):
        points = float(input("How many points do you want in your circle? (3 - 3000)"))
    print(f"You selected {points} points")

    times_table = int(input("What times table do you want to draw?"))
    radius = int(input("What radius would you like? 10-400"))
    '''
    points = 100
    times_table = 4
    radius = 400
    '''
    angle = 360 / points
    current_angle = 0
    for i in range(int(points)):
        point_coords = find_coord_of_point(radius, current_angle)
        circle_points.append(point_coords)
        current_angle = current_angle + angle
    print(circle_points)

    for i in range(int(points)):
        turtle.penup()
        turtle.goto(circle_points[i][0], circle_points[i][1])
        turtle.pendown()
        circle_point = round(((i*times_table) % points))
        turtle.goto(circle_points[int(circle_point)][0], circle_points[int(circle_point)][1])

    turtle.penup()
    turtle.home()
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.pensize(5)
    turtle.circle(radius)


main()

# Needed for pycharm to open the graphics windows
print(time.time()-start_time)
turtle.done()
