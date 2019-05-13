from tkinter import *
from gpiozero import LED
import RPi.GPIO as GPIO
root = Tk()
root.geometry("400x80")
root.title("LED on/off")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

v = IntVar()

led1 = LED(14)#8
led2 = LED(15)#10
led3 = LED(18)#12

def ledToggle1():
    if led1.is_lit:
        led1.off()

    else:
        led1.on()
    
def ledToggle2():        
    if led2.is_lit:
        led2.off()
        
    else:
        led2.on()

def ledToggle3():        
    if led3.is_lit:
        led3.off()
    
    else:
        led3.on()
def close():
    GPIO.cleanup()
    root.destroy()

blue = Radiobutton(root, text="Blue", command = ledToggle1, variable=v, value=1).pack(anchor ="w")
green = Radiobutton(root, text="Green", command = ledToggle2, variable=v, value=2).pack(anchor ="w")
red = Radiobutton(root, text="Red", command = ledToggle3, variable=v, value=3).pack(anchor ="w")

exit = Button(root, text = "Exit", command = close, bg = "red").pack(anchor ="center")

root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()
