from tkinter import *

window = Tk()
window.geometry("800x600+100+50")
window.configure(bg="white")

expression = ""
input_text = StringVar()

def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except Exception as e:
        input_text.set("Error")
        expression = ""

def btn_PlusMinus():
    global expression
    try:
        if expression:
            last_number = eval(expression)
            expression = str(-last_number)
            input_text.set(expression)
    except Exception as e:
        input_text.set("Error")
        expression = ""

def btn_result():
    try:
        result = str(eval(expression.replace("%","/100")))
        input_text.set(result)
        expression=""
    except:
        input_text.set("Error")
        expression = ""
    
frame_top = Frame(window, bg="black", width=500, height=300)
frame_top.pack(padx=0, pady=0)

frame_button = Frame(window, bg="black",width=600, height=0)
frame_button.pack(padx=10, pady=0)

label = Label(frame_top, text="Kalkulator Wildan K. XII PPLG 1", width=40, anchor="w", font=("Arial", 12))
label.pack(padx=0, pady=0)



window.mainloop()