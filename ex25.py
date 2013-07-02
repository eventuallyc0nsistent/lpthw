def break_words(things):
	"""This function breaks words for us"""
	words = things.split(' ')
	return words

def sort_words(things):
	"""Sorting words"""
	return sorted(things)

def print_first_words(things):
	"""Prints first word after popping it"""
	word = things.pop(0)
	print word

def print_last_word(things):
	"""Print last word popping it off"""
	word = things.pop(-1)
	print word

def sort_sentence(things):
	"""Taking full sentences to sort it"""
	word = break_words(things)
	return sort_words(things)

def print_first_and_last(things) :
	"""Prints first and last sentences"""
	word = break_words(things)
	print_first_words(word)
	print_last_word(word)

def print_first_and_last_sorted(things):
	"""Printing sorted first and last words"""
	word = sort_sentence(things)
	print_first_words(word)
	print_last_word(word)