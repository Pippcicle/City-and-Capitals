from tkinter import *
import random
from tkinter import messagebox

window = Tk()
window.title("Capital City quiz")

window.geometry("500x500+500+150")
window.configure(background="#B9D6F2")

main_lbl = Label(window, text="What's the capital city of... ", font=("ariel", 30, "bold"), bg="#B9D6F2", fg="#061A40").pack(pady=5)
questions_lbl = Label(window, font=("ariel", 22), bg="#B9D6F2", fg="#061A40").pack(pady=30, ipady=10, ipadx=10)

val = StringVar()
answerbox = Entry(window, textvariable=val, width=30).pack(ipadx=5, ipady=5)

check_btn = Button(window,text="Check",font=("ariel", 20, "bold"),width=10,bg="#0353A4",fg="#003559",).pack(pady=40)
reset_btn = Button(window,text="Reset",font=("ariel", 20, "bold"),width=10,bg="#006DAA",fg="#003559",).pack()

answers = ["Tirana","Andorra la Vella","Buenos Aires","Canberra","Vienna", "Dhaka", "Thimphu", "Gaborone", "Brasilia", "Phnom Penh", "Ottawa","N'Djamena","Santiago","Beijing","Bogota", "Copenhagen","Asmara", "Tallinn", "Paris", "Libreville", "Berlin", "Conakry", "New Delhi", "Tokyo", "Nairobi", "Riga", "Valletta", "Mexico City", "Kathmandu", "Abuja", "Oslo", "Manila", "Warsaw", "Moscow", "Singapore", "Seoul", "Dodoma", "Bangkok", "Ankara", "London", "Kyiv", "Hanoi"]
questions = ["Albania", "Andorra", "Argentina", "Australia", "Austria", "Bangladesh", "Bhutan", "Botswana", "Brazil", "Cambodia", "Canada", "Chad", "Chile", "China", "Colombia", "Denmark", "Eritrea", "Estonia", "France", "Gabon", "Germany", "Guinea", "India", "Italy", "Japan", "Kenya", "latvia", "Malta", "Mexico", "Nepal", "Nigeria", "Norway", "Philippines", "Poland", "Russia", "Singapore", "South Korea", "Tanzania", "Thailand","Turkey", "UK", "Ukraine", "Vietnam"]
num = random.randrange(0,len(questions),1)
score = 0
total = 0
s = ""

score_lbl = Label(window)



window.mainloop()
