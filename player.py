import pyautogui
from pykeyboard import PyKeyboard

def keyPress(input):
	print("input is:" + input)
	k = PyKeyboard()
	k.tap_key('1')
	# pyautogui.press(input)
		
