import pyautogui 
import time 

groups = ['4053991651383281']

time.sleep(5)
pyautogui.keyDown('ctrl')
pyautogui.keyDown('t')
pyautogui.keyUp('t')
pyautogui.keyUp('ctrl')

for i in range(len(groups)):
    link = 'https://www.facebook.com/groups/' + groups[i]
    pyautogui.typewrite(link)
    pyautogui.typewrite('\n')

    print("Espere 10 segundos... \n")
    time.sleep(10)

    print("Publicando ...")
    try:
        pyautogui.click('C:/Users/theot/Desktop/In process/FacebookPost/Img/b.png')
        time.sleep(4)
        pyautogui.typewrite("Prueba 2")
        time.sleep(4)
        pyautogui.click('C:/Users/theot/Desktop/In process/FacebookPost/Img/bimg.png')
        time.sleep(6)
        pyautogui.click('C:/Users/theot/Desktop/In process/FacebookPost/Img/nom.png')
        time.sleep(6)
        pyautogui.click('C:/Users/theot/Desktop/In process/FacebookPost/Img/env.png')
        time.sleep(6)
        pyautogui.click('C:/Users/theot/Desktop/In process/FacebookPost/Img/btn2.png')
        time.sleep(3)
        pyautogui.write(['f6'])
        time.sleep(3)
    except TypeError:
        print("Fatal error!")
   