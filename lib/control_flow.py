#!/usr/bin/env python3

def admin_login(username, password):
    if username.upper() == "ADMIN" and password == "12345":
        return "Access granted"
    
    return "Access denied"

def hows_the_weather(temperature):
    if temperature == 33:
        return "It's brisk out there!"
    elif temperature>33 and temperature <=55:
        return "It's a little chilly out there!"
    elif temperature >55 and temperature <=75:
        return "It's perfect out there!"
    else:
        return "It's too dang hot out there!"
   

def fizzbuzz(num):
    if not num % 15:
        return "FizzBuzz"
    elif not num % 5:
        return "Buzz"
    elif not num % 3:
        return "Fizz"
    
    return num

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2

    print("Invalid operation!")
    return None