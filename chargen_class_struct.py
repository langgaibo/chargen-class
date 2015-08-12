# wip  朗盖博 2015
from random import randint
prompt = '>: '

# prototyping the current class structure:
class Stats(object):

	def __init__(self):
		self.rolls = [self.basestat() for i in range(6)]

	def basestat(self):
		baseroll = [randint(1,6) for i in range(4)]
		delroll = min(baseroll)
		baseroll.remove(delroll)
		basestat = sum(baseroll)
		return basestat

	def get_rolls(self):
		return self.rolls

	# might need this later!
	def reroll(self):
		self.mulligan = [self.basestat() for i in range(6)]
		return self.mulligan

# define the Race classes
class Dragonborn(object):
	def __init__(self, stats):
		self.stats = stats
		self.indices = (0,5)
		self.values = (2,1)

	def output(self):
		return self.stats, self.indices, self.values

# map the classes as constants!!
race_choices = { 1:Dragonborn }
# pop these back in later
''', 2:Dwarf, 3:Elf,
4:Gnome, 5:Halfling, 6:Half-Elf,
7:Half-Orc, 8:Human, 9:Tiefling'''

# simple statprint function that can be called
# at different stages
def print_stats(stats):
	atts = [
	'Strength', 'Dexterity', 'Constitution',
	'Intelligence', 'Wisdom', 'Charisma']
	receipt = zip(atts, stats)
	print 'Current Stats:'
	print receipt

# take user selection and return
# the Class from race_choices
def picker():
	race_strings = [
		 '1. Dragonborn',
		'2. Dwarf', '3. Elf',
		'4. Gnome', '5. Halfling',
		'6. Half-Elf', '7. Half-Orc',
		'8. Human', '9. Tiefling'
		]
	print race_strings
	choice = int(raw_input(prompt))
	val = race_choices[choice]
	return val

# take (current_)stats and add Racial bonuses
def plus(stats, indices, values):
	dummy_list = [0,0,0,0,0,0]
	new_stats = stats
	for i in range(len(indices)):
		dummy_list[indices[i]] = values[i]
	for i in range(6):
		new_stats[i] += dummy_list[i]
	return new_stats

# Mint the class, peel off a layer, and print a receipt.
base = Stats()
current_stats = base.get_rolls()
print_stats(current_stats)

# might need to revert to base_stats later
base_stats = []
for i in range(len(current_stats)):
	base_stats.append(current_stats[i])

print 'Now choose a race.'
# chosen_race = binds the race Class itself
# rolled_instance = mints an instance of the
# chosen Class
chosen_race = picker()
rolled_instance = chosen_race(current_stats)


bonus = rolled_instance.output()
current_stats = plus(*bonus)
print_stats(current_stats)

# I would like to enforce this base class above the
# race subclasses, just for the sake of doing it.
'''
class Race(object):
	def __init__(self, stats):
	def __init__(self, stats):
		self.stats = stats
'''
