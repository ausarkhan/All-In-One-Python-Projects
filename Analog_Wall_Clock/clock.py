"""
Analog Wall Clock using Python Turtle and Threading
Issue #107 for king04aman/All-In-One-Python-Projects
"""
import turtle
import threading
import time
from datetime import datetime

WIDTH, HEIGHT = 600, 600

# Setup screen
def setup_screen():
    screen = turtle.Screen()
    screen.title("Analog Wall Clock")
    screen.bgcolor("white")
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.tracer(0)
    return screen

# Draw clock face
def draw_clock_face(clock_turtle):
    clock_turtle.penup()
    clock_turtle.goto(0, -250)
    clock_turtle.pendown()
    clock_turtle.pensize(5)
    clock_turtle.color("black")
    clock_turtle.circle(250)
    clock_turtle.penup()
    clock_turtle.goto(0, 0)
    clock_turtle.pendown()
    # Draw numbers
    for i in range(1, 13):
        angle = i * 30
        x = 200 * turtle.sin(turtle.radians(angle))
        y = 200 * turtle.cos(turtle.radians(angle))
        clock_turtle.penup()
        clock_turtle.goto(x, y-20)
        clock_turtle.pendown()
        clock_turtle.write(str(i), align="center", font=("Arial", 18, "bold"))
    # Decorative circles
    clock_turtle.penup()
    clock_turtle.goto(0, -220)
    clock_turtle.pendown()
    clock_turtle.pensize(2)
    clock_turtle.color("gray")
    clock_turtle.circle(220)
    clock_turtle.penup()
    clock_turtle.goto(0, -180)
    clock_turtle.pendown()
    clock_turtle.circle(180)
    clock_turtle.penup()
    clock_turtle.goto(0, 0)
    clock_turtle.pendown()

# Draw AM/PM indicator
def draw_ampm_indicator(clock_turtle):
    now = datetime.now()
    ampm = "AM" if now.hour < 12 else "PM"
    clock_turtle.penup()
    clock_turtle.goto(0, 120)
    clock_turtle.pendown()
    clock_turtle.color("blue")
    clock_turtle.write(ampm, align="center", font=("Arial", 16, "italic"))
    clock_turtle.penup()
    clock_turtle.goto(0, 0)
    clock_turtle.pendown()

# Hand drawing functions
def draw_hand(hand_turtle, length, angle, color, width):
    hand_turtle.clear()
    hand_turtle.penup()
    hand_turtle.goto(0, 0)
    hand_turtle.setheading(90)
    hand_turtle.right(angle)
    hand_turtle.pendown()
    hand_turtle.pensize(width)
    hand_turtle.color(color)
    hand_turtle.forward(length)
    hand_turtle.penup()
    hand_turtle.goto(0, 0)
    hand_turtle.pendown()

# Thread functions
def update_second_hand(hand_turtle):
    while True:
        now = datetime.now()
        angle = now.second * 6
        draw_hand(hand_turtle, 180, angle, "red", 2)
        time.sleep(0.1)

def update_minute_hand(hand_turtle):
    while True:
        now = datetime.now()
        angle = now.minute * 6 + now.second * 0.1
        draw_hand(hand_turtle, 150, angle, "black", 4)
        time.sleep(0.5)

def update_hour_hand(hand_turtle):
    while True:
        now = datetime.now()
        angle = (now.hour % 12) * 30 + now.minute * 0.5
        draw_hand(hand_turtle, 100, angle, "black", 6)
        time.sleep(1)

def main():
    screen = setup_screen()
    clock_turtle = turtle.Turtle()
    clock_turtle.hideturtle()
    clock_turtle.speed(0)
    draw_clock_face(clock_turtle)
    draw_ampm_indicator(clock_turtle)

    # Create turtles for hands
    sec_turtle = turtle.Turtle()
    sec_turtle.hideturtle()
    sec_turtle.speed(0)
    min_turtle = turtle.Turtle()
    min_turtle.hideturtle()
    min_turtle.speed(0)
    hour_turtle = turtle.Turtle()
    hour_turtle.hideturtle()
    hour_turtle.speed(0)

    # Start threads
    threading.Thread(target=update_second_hand, args=(sec_turtle,), daemon=True).start()
    threading.Thread(target=update_minute_hand, args=(min_turtle,), daemon=True).start()
    threading.Thread(target=update_hour_hand, args=(hour_turtle,), daemon=True).start()

    # Update AM/PM indicator every minute
    def update_ampm():
        while True:
            clock_turtle.clear()
            draw_clock_face(clock_turtle)
            draw_ampm_indicator(clock_turtle)
            time.sleep(60)
    threading.Thread(target=update_ampm, daemon=True).start()

    while True:
        screen.update()
        time.sleep(0.05)

if __name__ == "__main__":
    main()
