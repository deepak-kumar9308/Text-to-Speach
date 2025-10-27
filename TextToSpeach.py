import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import threading
import os

root = Tk()
root.title("Text to speech")
root.geometry("900x450+100+100")
root.resizable(False, False)
root.configure(bg='#305065')

def speaknow():
    text = text_area.get(1.0, END).strip()
    if not text:
        return

    gender = gender_combobox.get()
    speed = speed_combobox.get()

    def run_speech():
        try:
            # Create a fresh engine each time
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')

            # Gender selection
            if gender == 'Male':
                engine.setProperty('voice', voices[0].id)
            else:
                engine.setProperty('voice', voices[1].id)

            # Speed setting
            if speed == 'Fast':
                engine.setProperty('rate', 250)
            elif speed == 'Normal':
                engine.setProperty('rate', 150)
            else:
                engine.setProperty('rate', 60)

            engine.say(text)
            engine.runAndWait()
            engine.stop()
        except RuntimeError:
            try:
                new_engine = pyttsx3.init()
                new_engine.say(text)
                new_engine.runAndWait()
                new_engine.stop()
            except Exception as e:
                print("Error in reinitializing pyttsx3:", e)
    threading.Thread(target=run_speech, daemon=True).start()

def download():
    pass

# icon
image_icon = PhotoImage(file="./Assets/speak.png")
root.iconphoto(False, image_icon)

# Top Frame
Top_frame = Frame(root, bg='white', width=900, height=100)
Top_frame.place(x=0, y=0)

logo = PhotoImage(file='./Assets/speaker logo.png')
Label(Top_frame, image=logo, bg='white').place(x=10, y=5)

Label(Top_frame, text='TEXT TO SPEACH', font='arial 20 bold', bg='white', fg='black').place(x=100, y=30)

text_area = Text(root, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

Label(root, text='VOICE', font='arial 15 bold', bg='#305065', fg='white').place(x=580, y=160)
Label(root, text='SPEED', font='arial 15 bold', bg='#305065', fg='white').place(x=760, y=160)

gender_combobox = Combobox(root, values=['Male', 'Female'], font='arial 14', state='readonly', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

speed_combobox = Combobox(root, values=['Slow', 'Normal', 'Fast'], font='arial 14', state='readonly', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

imageicon = PhotoImage(file='./Assets/speak.png')
btn = Button(root, text='Speak', compound=LEFT, image=imageicon, width=130, font='arial 14 bold', command=speaknow)
btn.place(x=550, y=280)

imageicon2 = PhotoImage(file='./Assets/download.png')
save = Button(root, text='Save', compound=LEFT, image=imageicon2, width=130, bg='#39c790', font='arial 14 bold', command=download)
save.place(x=730, y=280)

# Footer
footer_label = Label(root, text="Made by Kr Deepak ❤️", font=('Arial', 10, 'italic'))
footer_label.place(x=720, y=420)

root.mainloop()
