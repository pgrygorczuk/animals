import pickle
from time import time

DB_FILE_NAME = 'db.pic'
ROOT		 = 'zwierzę lata'

db = {
	"zwierzę lata": { "y": "wróbel", "n": "pies" }
}

def save():
	with open(DB_FILE_NAME, 'wb') as f:
		pickle.dump(db, f)

try:
	with open(DB_FILE_NAME, 'rb') as f:
		db = pickle.load(f)
except:
	print('Database not found.')
	save()
	
def prepare_question(question):
	question = question.lower()
	if not question.startswith('czy to'):
		question = 'Czy to ' + question
	if not question.endswith('?'):
		question = question + '?'
	return question + ' [t/n]: '

def get_next_question(question, answer):
	if question not in db: return None
	return db[question]['y'] if answer else db[question]['n']

def play():
	prev_prev_question = None
	prev_question	   = None
	yn = prev_yn	   = None
	question		   = ROOT
	while question:
		prev_yn = yn
		yn = None
		prepared_question = prepare_question(question)
		while not yn in ('t', 'n'):
			yn = input( prepared_question )
		yn = yn.replace('t', 'y')
		prev_prev_question = prev_question
		prev_question = question
		question = get_next_question( question, yn=='y' )
	# Guessing is successful.
	if yn == 'y':
		print( ':-)' )
		return True
	# Can't guess, give up.
	answer		 = input( "Nie wiem co to może być. Napisz proszę jakie to zwierzę: " )
	new_question = input( "Jak byś opisał(a) to zwierzę? Napisz krótki opis, np. 'ma cztery łapy': " )
	prev_answer  = db[prev_prev_question][prev_yn]
	db[prev_prev_question][prev_yn] = new_question
	db[new_question] = {
		'y': answer,
		'n': prev_answer,
	}
	save()
	return False

	
if __name__ == '__main__':
	play()


# End of animals.py