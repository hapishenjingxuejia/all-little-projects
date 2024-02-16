import random
import easygui

easygui.msgbox("hello, I am ai 0.0010 , the quickest ai ever", "ai", "hello!")
easygui.msgbox("you can ask me any arithmetic problem, and I can put it down quickly.", "ai", "ok!")

state = 0
anw = ''

def add(a , b):
    global state, anw
    state = random.randint(0, 1)
    if state == 1:
        anw = int(a) + int(b)
        return anw
    else:
        return "I am the quickest , not the most accurate! 😀😀😀"

if add(easygui.enterbox("enter the first number","ai"), easygui.enterbox("enter the second number","ai")) != "I am the quickest , not the most accurate! 😀😀😀":
    if type(add(easygui.enterbox("enter the first number","ai"), easygui.enterbox("enter the second number","ai")) == "int" :
        easygui.msgbox("the answer is:" + str(add(easygui.enterbox("enter the first number","ai"), easygui.enterbox("enter the second number","ai")), "ai", "ok")
