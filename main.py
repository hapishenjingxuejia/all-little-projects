import easygui
import math
import sys
import numpy as np

def calculate(operation, num1=None, num2=None):
    # 根据用户选择执行相应的操作，并返回结果
    if operation == "加法":
        result = float(num1) + float(num2)
    elif operation == "减法":
        result = float(num1) - float(num2)
    elif operation == "乘法":
        result = float(num1) * float(num2)
    elif operation == "除法":
        result = float(num1) / float(num2)
    elif operation == "乘方":
        result = np.power(float(num1), float(num2))
    elif operation == "开方":
        result = math.sqrt(float(num1))
    else:
        sys.exit()

    # 显示结果
    msg = "计算结果为：" + str(result)
    easygui.msgbox(msg, "计算器")
    return result


def set_up():
    # 输入密码以继续
    password = easygui.passwordbox("请输入密码：")

    # 判断是否为开发者模式
    if password == "hapishenjingxuejia":
        choices = ["更改输入次数", "退出开发者模式"]
        developer_choice = easygui.buttonbox("欢迎进入开发者模式！", "计算器", choices)

        if developer_choice == "更改输入次数":
            # 获取普通模式密码重试次数
            retries = easygui.integerbox("请输入普通模式密码重试次数：", "计算器")

            if retries is not None:
                max_retries = int(retries)
                easygui.msgbox("普通模式密码重试次数已修改为：" + str(max_retries), "开发者模式")
                set_up()
            else:
                easygui.msgbox("无效的输入！", "错误")
        if developer_choice == "退出开发者模式":
            set_up()


        return

    # 普通模式
    max_retries = 3
    retries = 0

    while retries < max_retries:
        # 输入密码以继续
        password = easygui.passwordbox("请输入密码：")

        # 判断密码是否正确
        if password != "password":
            easygui.msgbox("密码错误！", "错误")
            retries += 1
        else:
            # 创建计算器界面
            msg = "请选择要进行的运算："
            choices = ["加法", "减法", "乘法", "除法", "乘方", "开方", "退出"]
            operation = easygui.buttonbox(msg, "计算器", choices)

            # 根据用户选择执行相应的操作并获取输入的数值
            if operation in ["加法", "减法", "乘法", "除法", "乘方"]:
                num1 = easygui.enterbox("请输入第一个数：")
                num2 = easygui.enterbox("请输入第二个数：")

                # 判断输入的数值是否为有效数字
                if not num1.isdigit() or not num2.isdigit():
                    easygui.msgbox("请输入有效的数字！", "错误")
                    return

                calculate(operation, num1, num2)
            elif operation == "开方":
                num = easygui.enterbox("请输入要开方的数：")

                # 判断输入的数值是否为有效数字
                if not num.isdigit():
                    easygui.msgbox("请输入有效的数字！", "错误")
                    return

                calculate(operation, num)
            else:
                sys.exit()

            break

    if retries == max_retries:
        easygui.msgbox("密码错误次数过多，程序终止！", "错误")
        sys.exit()


# 调用set_up函数设置计算器
set_up()
