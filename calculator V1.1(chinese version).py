import sys

import easygui


def addition(a, b):
    anw = int(a) + int(b)
    return str(anw)


def subtraction(a, b):
    anw = int(a) - int(b)
    return str(anw)


def choice_selector():
    choices = ["加法运算", "减法运算", "运算检查"]
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
    else:
        print("出错，马上关闭窗口，出错代码：C3.0x0007（选择未输入）")
        sys.exit()


if __name__ == "__main__":
    choice_selector()
