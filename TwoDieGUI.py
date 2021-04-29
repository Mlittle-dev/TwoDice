"""
program: TwoDieGUI.py
Author: Michael Little
"""

from breezypythongui import EasyFrame
import random

class TwoDice(EasyFrame):

	def __init__(self):
		EasyFrame.__init__(self, title = "TWO DICE GAME", resizable = False, background = "lightblue")
		self.addLabel(text = "TWO DICE GAME", row = 0, column = 0, columnspan = 5, sticky = "NSEW", background = "lightblue").config(font = ("Georgia", 16))
		self.addLabel(text = "Player dice: ", row = 1, column = 0, columnspan = 5, background = "lightblue")
		self.PlayerNum = self.addIntegerField(value = 0, row = 1, column = 2)
		self.addLabel(text = "COM dice: ", row = 2, column = 0, columnspan = 5, background = "lightblue")
		self.ComNum = self.addIntegerField(value = 0, row = 2, column = 2)
		
		self.addLabel(text = "Results: ", row = 5, column = 0, background = "lightblue")
		self.addButton(text = "Roll", row = 6, column = 0, columnspan = 5, command = self.pickNumbers)
		self.resultArea = self.addLabel(text = "",row = 5, column = 2)
		

	def pickNumbers(self):
		num1 = random.randint(1, 6)
		num2 = random.randint(1, 6)
		result = ""
		Player = self.PlayerNum.getNumber()
		com = self.ComNum.getNumber()

		if num1 < num2:
			result = "you lose"
			
		elif num1 > num2:
			result = "you win"
			
		else:
			result = "tie"

	

		self.PlayerNum.setNumber(num1)
		self.ComNum.setNumber(num2)
		self.resultArea["text"] = result



def main():
	
	TwoDice().mainloop()


main()