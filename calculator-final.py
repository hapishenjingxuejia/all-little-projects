import sys
import easygui
import random


def addition(a, b):
    try:
        anw = int(a) + int(b)
        return str(anw)
    except ValueError:
        return "请输入有效的数字"


def subtraction(a, b):
    try:
        anw = int(a) - int(b)
        return str(anw)
    except ValueError:
        return "请输入有效的数字"


def practice():
    question_number_1 = random.randint(1, 100)
    question_number_2 = random.randint(1, 100)
    right_answer = question_number_1 + question_number_2
    easygui.msgbox("题目是:" + str(question_number_1) + "+" + str(question_number_2) + "，请计算，完成后按ok按钮",
                   "计算练习")
    enter_ans = easygui.enterbox("输入你的答案", "计算练习")
    if right_answer == int(enter_ans):
        easygui.msgbox("做对了！真棒！😁😁😁😁😁")
    else:
        easygui.msgbox("做错了！😭😭😭😭😭" + "正确答案是" + str(right_answer))


def subtraction_practice():
    question_number_1 = random.randint(1, 100)
    question_number_2 = random.randint(1, 100)
    right_answer = question_number_1 - question_number_2
    easygui.msgbox("题目是:" + str(question_number_1) + "-" + str(question_number_2) + "，请计算，完成后按ok按钮",
                   "计算练习")
    enter_ans = easygui.enterbox("输入你的答案", "计算练习")
    if right_answer == int(enter_ans):
        easygui.msgbox("做对了！真棒！😁😁😁😁😁")
    else:
        easygui.msgbox("做错了！😭😭😭😭😭" + "正确答案是" + str(right_answer))


def choice_selector():
    choices = ["加法运算", "减法运算", "加法运算练习", "减法运算练习"]
    selected_choice = easygui.choicebox("请选择功能:", "计算器", choices=choices)

    if selected_choice:
        if selected_choice == "加法运算":
            x = easygui.enterbox("第一个加数：", "计算器")
            y = easygui.enterbox("第二个加数：", "计算器")
            easygui.msgbox(addition(x, y))

        if selected_choice == "减法运算":
            x = easygui.enterbox("第一个减数：", "计算器")
            y = easygui.enterbox("第二个减数：", "计算器")
            easygui.msgbox(subtraction(x, y))

        # 添加对“运算检查”选项的支持
        if selected_choice == "加法运算练习":
            practice()

        if selected_choice == "减法运算练习":
            subtraction_practice()

    else:
        print("出错，马上关闭窗口，出错代码：C3.0x0007（选择未输入）")
        sys.exit()


if __name__ == "__main__":
    choice_selector()
