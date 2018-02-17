import random 
def rand_word(): 
	a = input("What's your word?\n")
	return a 
	
shuffled = list(rand_word()) 
random.shuffle(shuffled) 
shuffled = ''.join(shuffled) 
print(shuffled)