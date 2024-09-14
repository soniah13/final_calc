import tkinter as tk
import math
from pygame import mixer
import speech_recognition
import threading

mixer.init()


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def rem(a, b):
    return a % b


def div(a, b):
    return a / b


def lcm(a, b):
    lm = math.lcm(a, b) if hasattr(math, 'lcm') else (a * b) // gcd(a, b)
    return lm


def gcd(a, b):
    gc = math.gcd(a, b)
    return gc


operations = {'+': add, 'ADD': add, 'PLUS': add, 'ADDITION': add, 'SUM': add,
              '-': sub, 'SUBTRACT': sub, 'MINUS': sub, 'DIFFERENCE': sub, 'SUBTRACTION': sub,
              '*': mul, 'MULTIPLY': mul, 'TIMES': mul, 'MULTIPLICATION': mul, 'PRODUCT': mul,
              '/': div, 'DIVIDE': div, 'DIVISION': div,
              'LCM': lcm, 'LOWEST_COMMON_MULTIPLE': lcm, 'GCD': gcd, 'GREATEST_COMMON_DIVIDER': gcd, 'HCF': gcd,
              '%': rem, 'MOD': rem, 'REMAINDER': rem, 'MODULUS': rem}


def find_numbers(t):
    num_l = []
    for num in t:
        try:
            num_l.append(int(num))
        except ValueError:
            pass
    return num_l


class Calculator:
    def __init__(self, window):
        self.window = window
        window.title('SONIA SCIENTIFIC CALCULATOR')
        window.geometry('610x500')

        self.total = tk.StringVar()

        try:
            self.logo = tk.PhotoImage(file='logo.png')
            self.logo_label = tk.Label(window, image=self.logo)
            self.logo_label.grid(row=0, column=0)
        except tk.TclError:
            print('Logo image not found.')

        self.entry_field = tk.Entry(window, textvariable=self.total, relief='groove', bg='silver', font=('Arial', 20))
        self.entry_field.grid(row=0, column=0, columnspan=8, pady=5)

        try:
            self.mic_image = tk.PhotoImage(file='microphone.png')
            self.mic_button = tk.Button(window, image=self.mic_image, bd=0, bg='deepskyblue', command=self.audio,
                                        activebackground='deepskyblue')
            self.mic_button.grid(row=0, column=7)
        except tk.TclError:
            print('Microphone image not found')

        self.create_buttons()

    def create_buttons(self):
        button_list = [
                       ['C', 'CE', '√', '+', 'π', 'cos', 'tan', 'sin'],
                       ['1', '2', '3', '-', '2π', 'cosh', 'tanh', 'sinh'],
                       ['4', '5', '6', '*', chr(8731), 'x\u02b8', 'x\u00B3', 'x!'],
                       ['ln', '7', '8', '9', '/', 'deg', 'rad', 'e'],
                       [',', '0', '. ', '%', '=', 'log(x)', '(', ')']
        ]

        for i, row in enumerate(button_list):
            for j, button_text in enumerate(row):
                button = tk.Button(
                    self.window, text=button_text, width=5, height=3, bg='lavenderblush', font=('Calibre', 18),
                    command=lambda text=button_text: self.click(text)
                )
                button.grid(row=i+1, column=j, sticky='nsew')
            self.window.rowconfigure(i+1, weight=1)
        for i in range(8):
            self.window.columnconfigure(i, weight=1)

    def click(self, button_text):
        if button_text == 'CE':
            self.total.set('')
        elif button_text == 'C':
            current_text = self.entry_field.get()
            if current_text:
                new_text = current_text[:-1]
                self.total.set(new_text)
        elif button_text == '=':
            try:
                result = eval(self.entry_field.get())
                self.total.set(result)
            except:
                self.total.set('ERROR!')
        elif button_text == 'sin':
            try:
                result = math.sin(math.radians(float(self.entry_field.get())))
                self.total.set(result)
            except:
                self.total.set('ERROR!')
        elif button_text == 'cos':
            try:
                result = math.cos(math.radians(float(self.entry_field.get())))
                self.total.set(result)
            except:
                self.total.set('ERROR!')
        elif button_text == 'tan':
            try:
                result = math.tan(math.radians(float(self.entry_field.get())))
                self.total.set(result)
            except:
                self.total.set('ERROR!')
        elif button_text == 'tanh':
            try:
                result = math.tanh(float(self.entry_field.get()))
                self.total.set(result)
            except:
                self.total.set('ERROR!')
        elif button_text == 'sinh':
            try:
                result = math.sinh(float(self.entry_field.get()))
                self.total.set(result)
            except:
                self.total.set('ERROR!')
        elif button_text == 'cosh':
            try:
                result = math.cosh(float(self.entry_field.get()))
                self.total.set(result)
            except:
                self.total.set('ERROR!')
        elif button_text == 'x\u02b8':
            try:
                current_text = self.entry_field.get()
                self.total.set(current_text + '**')
            except:
                self.total.set('ERROR!')
        elif button_text == '√':
            try:
                result = math.sqrt(float(self.entry_field.get()))
                self.total.set(result)
            except:
                self.total.set('ERROR!')
        elif button_text == 'x!':
            try:
                result = math.factorial(int(self.entry_field.get()))
                self.total.set(result)
            except:
                self.total.set('ERROR!')
        elif button_text == 'x\u00B3':
            try:
                result = float(self.entry_field.get()) ** 3
                self.total.set(result)
            except:
                self.total.set('ERROR!')
        elif button_text == 'log(x)':
            try:
                result = math.log(float(self.entry_field.get()))
                self.total.set(result)
            except:
                self.total.set('ERROR!')
        elif button_text == 'ln':
            try:
                result = math.log(float(self.entry_field.get()))
                self.total.set(result)
            except:
                self.total.set('ERROR!')
        elif button_text == 'rad':
            try:
                result = math.radians(float(self.entry_field.get()))
                self.total.set(result)
            except:
                self.total.set('ERROR!')
        elif button_text == 'deg':
            try:
                result = math.degrees(float(self.entry_field.get()))
                self.total.set(result)
            except:
                self.total.set('ERROR!')
        elif button_text == 'e':
            try:
                result = math.e
                self.total.set(result)
            except:
                self.total.set('ERROR!')
        elif button_text == 'π':
            try:
                result = math.pi
                self.total.set(result)
            except:
                self.total.set('ERROR!')
        elif button_text == '2π':
            try:
                result = math.pi * 2
                self.total.set(result)
            except:
                self.total.set('ERROR!')
        elif button_text == chr(8731):
            try:
                result = float(self.entry_field.get()) ** 1/3
                self.total.set(result)
            except:
                self.total.set('ERROR!')
        elif button_text == '%':
            try:
                current_value = float(self.entry_field.get())
                result = current_value * 100
                self.total.set(f'{result}%')
            except:
                self.total.set('ERROR!')
        else:
            self.total.set(self.entry_field.get() + button_text)

    def audio(self):
        def run_audio():
            try:
                mixer.music.load('music1.mp3')
                mixer.music.play()
                speak = speech_recognition.Recognizer()
                with speech_recognition.Microphone() as m:
                    speak.adjust_for_ambient_noise(m, duration=0.2)
                    voice = speak.listen(m)
                    text = speak.recognize_google(voice)
                    mixer.music.load('music2.mp3')
                    mixer.music.play()
                    text_list = text.split(' ')
                    print(text_list)
                    for word in text_list:
                        if word.upper() in operations.keys():
                            num_l = find_numbers(text_list)
                            print(num_l)
                            if len(num_l) >= 2:
                                try:
                                    result = operations[word.upper()](num_l[0], num_l[1])
                                    self.entry_field.delete(0, -1)
                                    self.entry_field.insert(-1, result)
                                except:
                                    self.total.set('ERROR!')
                        else:
                            pass
            except Exception as e:
                print(f'Error:{e}')
    
        threading.Thread(target=run_audio).start()


if __name__ == '__main__':
    root = tk.Tk()
    my_calc = Calculator(root)
    root.mainloop()
