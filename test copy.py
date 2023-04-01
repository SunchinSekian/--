a=[]
b=[]
import pyautogui
while True:
    c=input('输入单词')
    if c=='ESC':
        break
    pyautogui.press('shift')
    d=input('输入中文：')
    pyautogui.press('shift')
    a.append(c)
    b.append(d)
with open('words.txt','a+',encoding='UTF-8') as f:
    for i in range(len(a)):
        f.write(a[i]+','+b[i]+'\n')
