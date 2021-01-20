import pyautogui 
import time 

f = open('C:/Users/theot/Desktop/Cosas/Programacion/Python/FacebookPost/texto.txt','r')
post = (f.read())

groups = ['4053991651383281']

imagenes = ['C:/Users/theot/Desktop/Cosas/Programacion/Python/FacebookPost/Img/p1.png', 
'C:/Users/theot/Desktop/Cosas/Programacion/Python/FacebookPost/Img/p2.png', 
'C:/Users/theot/Desktop/Cosas/Programacion/Python/FacebookPost/Img/p3.png' ]

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
        pyautogui.click('C:/Users/theot/Desktop/Cosas/Programacion/Python/FacebookPost/Img/b.png') # Boton post
        time.sleep(2)
        pyautogui.typewrite(post) # Texto Post
        time.sleep(4)
        pyautogui.click('C:/Users/theot/Desktop/Cosas/Programacion/Python/FacebookPost/Img/bimg.png') # Btn img
        time.sleep(3)

        for i in range(len(imagenes)):
            try:
                pyautogui.click('C:/Users/theot/Desktop/Cosas/Programacion/Python/FacebookPost/Img/bimg2.png') # Btn img
                time.sleep(3)
                pyautogui.click(imagenes[i]) # Img
                time.sleep(3)
                pyautogui.click('C:/Users/theot/Desktop/Cosas/Programacion/Python/FacebookPost/Img/env.png') # Enviar
                time.sleep(3)
            except:
                pyautogui.click(imagenes[i]) # Img
                time.sleep(3)
                pyautogui.click('C:/Users/theot/Desktop/Cosas/Programacion/Python/FacebookPost/Img/env.png') # Enviar
                time.sleep(3)

        pyautogui.click('C:/Users/theot/Desktop/Cosas/Programacion/Python/FacebookPost/Img/btn2.png') # Publicar
        time.sleep(3)
        pyautogui.write(['f6'])
        time.sleep(3)
    except TypeError:
        print("Fatal error! \n")
   