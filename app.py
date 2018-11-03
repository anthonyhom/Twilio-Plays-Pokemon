from flask import Flask, request
import player 
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

dictionary = {'up': 'w', 'down' : 's'}
@app.route('/sms', methods = ["GET","POST"])

def sms():
	body = request.values.get('Body', None)
	resp = MessagingResponse()
	if body not in dictionary:
		resp.message('\n Move/Scroll Up: W, \n Move Left: A, \n Move Right: D, \n Move/Scroll Down: S, \n Open Menu: L, \n Select: R, \n Go Back: T')
	else:
		player.keyPress(dictionary['message_body'])
	return str(resp)

if __name__ == '__main__':
	app.run(debug=True)	