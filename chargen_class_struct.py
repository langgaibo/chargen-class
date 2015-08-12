# prototyping the current class structure:
from random import randint
prompt = '>: '

# simple statprint function that can be called
# at different stages
def print_stats(stats):
	atts = [
	'Strength', 'Dexterity', 'Constitution',
	'Intelligence', 'Wisdom', 'Charisma']
	receipt = zip(atts, stats)
	print 'Current Stats:'
	print receipt

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

class Dragonborn(object):
	def __init__(self, stats):
		self.stats = stats
		self.indices = (0,5)
		self.values = (2,1)

	def output(self):
		return self.stats, self.indices, self.values

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

# temporary railroading of the intended choice flow
choice = Dragonborn(current_stats)
data = choice.output()
outcome = plus(*data)
print_stats(outcome)

################################
#  BELOW LIES A GARBAGE DUMP!  #
################################

# I DEMAND that this dictionary works
race_choices = {
	1:'Dragonborn', 2:'Dwarf', 3:'Elf',
	4:'Gnome', 5:'Halfling', 6:'Half-Elf',
	7:'Half-Orc', 8:'Human', 9:'Tiefling'
	}

# a disgusting and failed attempt at not using a big if block for this choice.
'''
def picker():
	print race_choices
	print 'Pick a number to select a class.'
	choice = int(raw_input(prompt))
	val = race_choices.get[choice]
	# horrible
	wrap = '%s(current_stats)'
	exec wrap
'''
# I would like to enforce this base class above the
# race subclasses, just for the sake of doing it.
'''
class Race(object):
	def __init__(self, stats):
	def __init__(self, stats):
		self.stats = stats
'''
