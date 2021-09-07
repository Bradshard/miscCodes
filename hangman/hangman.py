import random

easy_mode = 'hangman_easy.txt'
hard_mode = 'hangman_hard.txt'

def get_word(word_list):
	with open(word_list,'r') as dosya:
		liste = dosya.readlines()
		liste = [i.strip() for i in liste]
	return random.choice(liste).lower()

def control_words(word,used_words,psychic):
	location = []
	pairments = 0
	for i in word:
		if i in used_words:
			location.append(i)
		else:
			location.append('#')
		if i == psychic:
			pairments += 1

	if (pairments > 1):
		print("Hurray! Word has them. You little psychic.", pairments, '"', psychic, '"' + 's')
	elif (pairments == 1):
		print("Here as in the Wheel Of Fortune, we open one letter for you, after the finger.", psychic, '"')
	else:
		print("Aaah, so sad. There isn't of that letter but your chance at getting your loans paid still goes.'", psychic, '"')
	return "".join(location)

def hangman(liste):
	word = get_word(liste)
	used_words = []
	not_find = True
	print("Word has",len(word),"letters.")
	global num_attempt

	while not_find and num_attempt > 0:
		message = """Please enter a letter.
Type here: """
		psychic = input(message)
		psychic = psychic.lower()
		if not psychic.isalpha():
			print("we can only use letters not numbers or special characters")
			continue
		if (psychic in used_words):
			print("Don't give me used words.")
		elif (len(psychic) == 1):
			used_words.append(psychic)
			aftermath = control_words(word,used_words,psychic)
			if aftermath == word:
				not_find = False
			else:
				print(aftermath)
				if psychic not in word:
					num_attempt -= 1
					print("""Remaining attempts: {}""".format(num_attempt))

		elif len(psychic) == len(word):
			used_words.append(psychic)
			if psychic == word:
				not_find = False
			else:
				num_attempt -= 1
				print("""Remaining attempts: {}""".format(num_attempt))

		else:
			num_attempt -= 1
			print("""It's an invalid entry, that made me cry a little.
				Remaining attempts: {}""".format(num_attempt))
	if num_attempt != 0 :
		print("Finally found it dude! The word is:", word)
	else:
		print("You couldn't find it!","\n word was {}".format(word))

num_attempt = 10
print("""Are you a true psychic,
then show me your powers. You have only 6 chances to
prove your mighty. Find the word or find it
letter by letter. Good luck, Youngling.""")
hangman(easy_mode)
while True:
	last_sentence = input("""Do you want to play again?
	If you want press Y/y, if you don't press N/n.""")
	if last_sentence == "y" or last_sentence == "Y":
		hardness = input("""So you really believe your guts than prove it on the hard level.
If you choose hard game, press H/h. Or if you are just a bystander type ez/EZ.""")
		if hardness == "H" or hardness == "h":
			num_attempt = 6
			hangman(hard_mode)
		elif hardness == "ez" or hardness =="EZ":
			num_attempt = 10
			hangman(easy_mode)
	elif last_sentence == "n" or last_sentence == "N":
		break
