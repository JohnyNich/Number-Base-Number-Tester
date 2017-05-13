import tkinter
import random

window = tkinter.Tk()
window.title("Binary and Hex number tester")
window.geometry("550x200")

lbl_welcome = tkinter.Label(window, text = "Welcome!")
numberbase = tkinter.StringVar(window) # strvar is short for StringVar.
numberbase.set("Please select a numberbase...")
dropdown_numerbase = tkinter.OptionMenu(window, numberbase, "Binary", "Hexidecimal")
difficulty = tkinter.StringVar(window)
difficulty.set("Please select a difficulty...")
dropdown_difficulty = tkinter.OptionMenu(window, difficulty, "Easy", "Medium", "Hard", "Extreme")
lbl_question = tkinter.Label(window, text = "Please select the above boxes and click Play to get a question")
entry = tkinter.Entry(window)
lbl_score = tkinter.Label(window, text = "Score: 0")
btn_play = tkinter.Button(window, text = "Play!")

def play():
	# This generates the number
	if difficulty.get() == "Easy":
		number = random.randint(1, 30)
	elif difficulty.get() == "Medium":
		number = random.randint(1, 100)
	elif difficulty.get() == "Hard":
		number = random.randint(1, 500)
	else: # Else would be Extreme, as it's the only option which doesn't have a conditional stated above
		number = random.randint(1, 1000)
	# This creates the question
	if numberbase.get() == "Binary":
		if random.randint(0, 1) == 0:
			lbl_question.configure(text = "Translate " + str(number) + " to binary.")
			answer = bin(number)
		else: # This is if random.randint is 1
			lbl_question.configure(text = "Translate " + str(bin(number)) + " to a normal integer.")
			answer = number
	else: # This is if the user inputs Hexidecimal as the numberbase
		if random.randint(0, 1) == 0:
			lbl_question.configure(text = "Translate " + str(number) + " to hexidecimal")
			answer = hex(number)
		else: # This is if random.randint is 1
			lbl_question.configure(text = "Translate " + str(hex(number)) + " to a normal integer.")
			answer = number

btn_play.configure(command = play)

lbl_welcome.grid(row = 0, column = 1)
dropdown_numerbase.grid(row = 1, column = 0)
dropdown_difficulty.grid(row = 1, column = 2)
lbl_question.grid(row = 2, columnspan = 3)
entry.grid(row = 3, columnspan = 3)
lbl_score.grid(row = 4, column = 1)
btn_play.grid(row = 5, column = 1)

window.mainloop()
