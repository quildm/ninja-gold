from random import randrange
import datetime
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "TotallyNotSecret"

@app.route('/')
def landing_page():
	# The try/except block runs some code to access the key 'gold' in the session dictionary. If the code causes a KeyError, then the code in the except block runs which gives it an initial value.
	try:
		session['gold']
		print ("I have gold already")
	except KeyError:
		session['gold'] = 0
	try:
		session['messages']
	except KeyError:
		session['messages'] = []
	return render_template('landing_page.html')

@app.route('/process_money', methods=["POST"])
def process():
	print (request.form["building"])
	location = request.form['building']
	# Refer to the video to see how I refactored this code.
	if location == "farm":
		gold_earned = randrange(10,21)
	elif location == "cave":
		gold_earned = randrange(5,11)
	elif location == "house":
		gold_earned = randrange(2,6)
	elif location == "casino":
		gold_earned = randrange(-50,50)
	# We want to represent the color of the text as a part of the message. Since the message is now something more than the text on the screen, we want a container data structure (list, tuple, object, or dictionary) as the individual item in the session['messages'] list
	session['gold'] += gold_earned
	if gold_earned < 0:
		color = "red"
		new_string = "Went to casino and lost "+str(-gold_earned)+" gold. Ouch! "+str(datetime.datetime.now()) # remember to concatenate the numbers to the string after you convert them into strings!
	else:
		color = "green"
		new_string = "Went to "+location+" and got "+str(gold_earned)+" gold. "+str(datetime.datetime.now())
	new_dictionary = {
	"color":color,
	"message":new_string
	}
	session['messages'].insert(0,new_dictionary)

	print ("****************")
	print (session['gold'])
	print ("****************")
	print (session['messages'])
	return redirect('/')

app.run(debug=True)