import random
def ask_b_g():
	a = input(str("b or g?\n"))
	if (a == "b"):
		Name = [
		'Dalton',
		'Jamal',
		'Kyle',
		'Tommy',
		'Owen',
		]
		
	else:
		Name= [
		'Ariana',
		'Jayla',
		'Faile',
		'Jaida',
		'Savannah',
		]
	return random.choice(Name)
def pick_race():
	Race= [
	'human',
	'elf',
	'ork',
	'Dwarf',
	'half elf',
	'half ork',
	'gnome',
	'halfing',
	]
	return random.choice(Race)
def pick_class():
	Class= [
	'fighter',
	'druid',
	'barbaran',
	'bard',
	'wizard',
	'ranger',
	'paladin',
	'sorcorer',
	'monk',
	]
	return random.choice(Class)
print(ask_b_g())
print(pick_race())
print(pick_class()) 