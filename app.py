from flask import Flask, request
import player 
from twilio.twiml.messaging_response import MessagingResponse
from pykeyboard import PyKeyboard
import time

app = Flask(__name__)

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


if __name__ == '__main__':
	app.run(debug=True)	