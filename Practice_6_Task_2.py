# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,. приоритет операций стандартный.
import datetime

def WriteListToFile(fileName, textData):
    todayDateTime = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    textData ='' + todayDateTime + '- The result of the expression is ' + str(textData) + '\n'
    with open(fileName, "a") as file:
       file.write(textData)
       file.close

def StrParse(str):
    lenght = len(str)
    flag = False
    operand_1_str = ''
    operand_2_str = ''
    for i in range (lenght):
        if str[i].isdigit() or (str[i]=='-' and i==0):  # пока элемент строки является числом добавляем его к операнту 1
            if flag == False:
                operand_1_str = operand_1_str+str[i]
        else:
            flag = True
            operation = str[i]  # если элемент строки не число, значит запоминаем его как знак операции
            break
    for i in reversed(str):  # просматриваем строку с конца, чтобы сформировать оперант 2
        if i.isdigit():
            if flag == True:
                operand_2_str = operand_2_str+i
        else:
            flag = False
            break
    operand_1 = float(operand_1_str)
    operand_2 = float(operand_2_str[::-1])#разворачивает строку, т.к. в цикле она вызывалась с конца
    return [operand_1, operand_2, operation]

def GetOperation(operands):
    match operands[2]:
        case '+':
            result = operands[0]+operands[1]
        case '-':
            result = operands[0]-operands[1]
        case '/':
            try:
                result = operands[0]/operands[1]
            except ZeroDivisionError:
                print("Check your input! Zero division was detected!")
                return None
        case '*':
            result=operands[0]*operands[1]
    return result

inputStr=input("Enter your expression, for instance, '22+9': ")
operands=StrParse(inputStr)
result=GetOperation(operands)
WriteListToFile('LogData.txt',result)
print(f"The result of the expression {inputStr} is {result}")