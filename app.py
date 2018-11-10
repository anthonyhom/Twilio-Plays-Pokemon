from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pykeyboard import PyKeyboard
import time
from twilio.twiml.voice_response import VoiceResponse, Gather, Say 


app = Flask(__name__)
dictionary = {'Up': 'w', 'Down' : 's', 'Left' : 'a', 'Right' : 'd', 'Start' : 'r', 'Select' : 't', 'A' : '1', 'B' : '2', 'L' : 'q', 'R' : 'e', 'X' : 'x', 'Y' : 'y'}

@app.route('/sms', methods = ["GET","POST"])
def sms():
	body = request.values.get('Body', None)
	resp = MessagingResponse()
	k = PyKeyboard()
	if body not in dictionary:
		resp.message('\n Move/Scroll Up: Up , \n Move Left: Left, \n Move Right: Right, \n Move/Scroll Down: Down, \n Start: Start, \n Select : Select, \n A : A, \n B: B, \n L : L, \n R : R')
	else:
		k.press_key(dictionary[body])
		time.sleep(0.1)
		k.release_key(dictionary[body])
	return str(resp)

if __name__ == '__main__':
	app.run(debug=True)	