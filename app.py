from flask import Flask, request
import player 
from twilio.twiml.messaging_response import MessagingResponse
from pykeyboard import PyKeyboard
import time
from flask_ask import statement, Ask
from twython import TwythonStreamer

app = Flask(__name__)
ask = Ask(app, '/')
dictionary = {'Up': 'w', 'Down' : 's', 'Left' : 'a', 'Right' : 'd', 'Start' : 'r', 'Select' : 't', 'A' : '1', 'B' : '2', 'L' : 'q', 'R' : 'e'}


@app.route('/sms', methods = ["GET","POST"])
def sms():
	body = request.values.get('Body', None)
	resp = MessagingResponse()
	k = PyKeyboard()
	if body not in dictionary:
		resp.message('\n Move/Scroll Up: W, \n Move Left: A, \n Move Right: D, \n Move/Scroll Down: S, \n Open Menu: L, \n Select: R, \n Go Back: T')
	else:
		k.press_key(dictionary[body])
		time.sleep(0.1)
		k.release_key(dictionary[body])
	return str(resp)
'''
@ask.intent('game')
def alexa_plays(commands, convert = {'commands' : str}):
	return statement('Hello')
	data = request.slots('commands')
	data = commands 
	if data == 'up':
		k.press_key(dictionary['Up'])
		time.sleep(0.1)
		k.release_key(dictionary['Up'])
	elif data == 'down':
		k.press_key(dictionary['Down'])
		time.sleep(0.1)
		k.release_key(dictionary['Down'])
	elif data == 'left':
		k.press_key(dictionary['Left'])
		time.sleep(0.1)
		k.release_key(dictionary['Left'])
	elif data == 'right':
		k.press_key(dictionary['Right'])
		time.sleep(0.1)
		k.release_key(dictionary['Right'])
	elif data == 'a':
		k.press_key(dictionary['A'])
		time.sleep(0.1)
		k.release_key(dictionary['A'])
	elif data == 'b':
		k.press_key(dictionary['B'])
		time.sleep(0.1)
		k.release_key(dictionary['B'])
	elif data == 'start':
		k.press_key(dictionary['Start'])
		time.sleep(0.1)
		k.release_key(dictionary['Start'])
	elif data == 'select':
		k.press_key(dictionary['Select'])
		time.sleep(0.1)
		k.release_key(dictionary['Select'])
	elif data == 'l':
		k.press_key(dictionary['L'])
		time.sleep(0.1)
		k.release_key(dictionary['L'])
	else:
		k.press_key(dictionary['R'])
		time.sleep(0.1)
		k.release_key(dictionary['R'])
	return statement('Ayo')
'''

if __name__ == '__main__':
	app.run(debug=True)	