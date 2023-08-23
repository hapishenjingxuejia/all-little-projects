import easygui

# 创建一个函数，用于处理计算逻辑
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return None  # 返回None表示除数为0错误

while True:
    try:
        # 使用easygui创建输入框获取用户输入
        num1 = easygui.enterbox("请输入第一个数字:")
        operator = easygui.enterbox("请输入运算符 (+, -, *, /):")
        num2 = easygui.enterbox("请输入第二个数字:")

        # 检查是否有输入为空
        if not num1 or not operator or not num2:
            raise ValueError("输入不能为空")

        # 将用户输入转换为数值类型
        num1 = float(num1)
        num2 = float(num2)

        # 调用calculate函数进行计算
        result = calculate(num1, num2, operator)

        # 检查除数为0的错误
        if result is None:
            raise ZeroDivisionError("错误：除数不能为0")

        # 使用easygui显示计算结果
        easygui.msgbox(f"计算结果为: {result}")
        break  # 计算成功，退出循环

    except ValueError as e:
        easygui.msgbox(str(e))
    except ZeroDivisionError as e:
        easygui.msgbox(str(e))
