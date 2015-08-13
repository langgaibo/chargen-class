# coding: utf8
# wip  朗盖博 2015
from random import randint
prompt = '>: '

# Inits with a list of rolled stats,
# which can be retrieved or rerolled
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

# Base class serves 2 purposes:
# 1. Teaching me basic inheritance
# 2. output() method call so I don't have to write it 9x
class Race(object):
	def __init__(self, stats):
		self.stats = stats
	def output(self):
		self.subrace()
		return self.stats, self.indices, self.values

# Subclasses all call Parent.__init__ to mint themselves
# with inherited stats.
class Dragonborn(Race):
	def __init__(self, stats):
		Race.__init__(self, stats)
		print '\nDragonborn get +2 Str, +1 Cha! Put on some lotion, scales!'
	def subrace(self):
		self.race = 'Dragonborn'
		self.indices = (0,5)
		self.values = (2,1)

# Some subclasses require user input to define
# bonuses, so the parent class triggers this with the
# output() method.
class Dwarf(Race):
	def __init__(self, stats):
		Race.__init__(self, stats)
		print '\nAll Dwarves get +2 Constitution, beardo!'
	def subrace(self):
		print 'Select a subrace!'
		print '"h" for Hill Dwarf (+1 Wis),'
		print '"m" for Mountain Dwarf (+2 Str)'
		sub_choice = raw_input(prompt)
		if sub_choice == 'h':
			self.race = 'Hill Dwarf'
			self.indices = (2,4)
			self.values = (2,1)
		elif sub_choice == 'm':
			self.race = 'Mountain Dwarf'
			self.indices = (0,2)
			self.values = (2,2)
		else:
			print '\nWhat?'
			self.subrace()

class Elf(Race):
	def __init__(self, stats):
		Race.__init__(self, stats)
		print '\nAll Elves get +2 Dex, pointy!'
	def subrace(self):
		print 'Select a subrace!'
		print '"h" for High Elf (+1 Int),'
		print '"w" for Wood Elf (+1 Wis),'
		print '"d" for Drow (+1 Cha)'
		sub_choice = raw_input(prompt)
		if sub_choice == 'h':
			self.race = 'High Elf'
			self.indices = (1,3)
			self.values = (2,1)
		elif sub_choice == 'w':
			self.race = 'Wood Elf'
			self.indices = (1,4)
			self.values = (2,1)
		elif sub_choice == 'd':
			self.race = 'Drow'
			self.indices = (1,5)
			self.values = (2,1)
		else:
			print 'What?'
			self.subrace()

class Gnome(Race):
	def __init__(self, stats):
		Race.__init__(self, stats)
		print '\nAll Gnomes get +2 Int, Gizmo!'
	def subrace(self):
		print 'Select a subrace!'
		print '"f" for Forest Gnome (+1 Dex),'
		print '"r" for Rock Gnome (+1 Con)'
		sub_choice = raw_input(prompt)
		if sub_choice == 'f':
			self.race = 'Forest Gnome'
			self.indices = (3,1)
			self.values = (2,1)
		elif sub_choice == 'r':
			self.race = 'Rock Gnome'
			self.indices = (3,2)
			self.values = (2,1)
		else:
			print 'What?'
			self.subrace()

class Halfling(Race):
	def __init__(self, stats):
		Race.__init__(self, stats)
		print '\nAll Halflings get +2 Dex, Samwise!'
	def subrace(self):
		print 'Select a Clan!'
		print '"l" for Lightfoot (+1 Cha),'
		print '"s" for Stout (+1 Con)'
		sub_choice = raw_input(prompt)
		if sub_choice == 'l':
			self.race = 'Lightfoot Clan Halfling'
			self.indices = (1,5)
			self.values = (2,1)
		elif sub_choice == 's':
			self.race = 'Stout Clan Halfling'
			self.indices = (1,2)
			self.values = (2,1)
		else:
			print 'What?'
			self.subrace()

class Half_Elf(Race):
	def __init__(self, stats):
		Race.__init__(self, stats)
		self.statdict = {'str':0, 'dex':1, 'con':2, 'int':3, 'wis':4, 'cha':5}
	def subrace(self):
		self.race = 'Half-Elf'
		print_stats(self.stats)
		print '\nHalf-Elves get +2 Cha, as well as +1 to two separate stats of your choice.'
		print '\nNow, type the abbreviated name of the first stat to +1 (i.e. "str").'
		self.first = str(raw_input(prompt))
		print '\n...now type the second stat to +1.'
		print 'Don\'t double up!'
		self.second = str(raw_input(prompt))
		# bug check
		if self.first == self.second:
			print '\nNo cheating!'
			print 'Try again.\n\n'
			self.subrace()
		if self.first in self.statdict:
			if self.second in self.statdict:
				pass
			else:
				print '\nWhat?'
				print 'Try again.\n\n'
				self.subrace()
		else:
			print '\nWhat?'
			print 'Try again.\n\n'
			self.subrace()
		stat1 = self.statdict[self.first]
		stat2 = self.statdict[self.second]
		# If they chose Cha, make sure to overwrite with +3
		# otherwise append it. Lists are ok instead of tuples
		self.indices = [stat1,stat2]
		self.values = [1,1]
		if self.first == 'cha':
			self.values[0] = 3
		elif self.second == 'cha':
			self.values[1] = 3
		else:
			self.indices = [stat1,stat2,5]
			self.values = [1,1,2]


class Half_Orc(Race):
	def __init__(self, stats):
		Race.__init__(self, stats)
		print '\nHalf-Orcs get +2 Str, +1 Con, you ugly motherfucker!'
	def subrace(self):
		self.race = 'Half-Orc'
		self.indices = (0,2)
		self.values = (2,1)

class Human(Race):
	def __init__(self, stats):
		Race.__init__(self, stats)
		print '\nHumans get +1 across the board! Patriarchs!'
	def subrace(self):
		self.race = 'Human'
		self.indices = (0,1,2,3,4,5)
		self.values = (1,1,1,1,1,1)

class Tiefling(Race):
	def __init__(self, stats):
		Race.__init__(self, stats)
		print '\nTieflings get +1 Int, +2 Cha, Tinkerbell!'
	def subrace(self):
		self.race = 'Tiefling'
		self.indices = (3,5)
		self.values = (1,2)

# map the classes as constants. I refused to write a big if block :)
race_choices = {
	1:Dragonborn,
	2:Dwarf,
	3:Elf,
	4:Gnome,
	5:Halfling,
	6:Half_Elf,
	7:Half_Orc,
	8:Human,
	9:Tiefling
	}

# take user selection and return the Class from race_choices
def picker():
	race_strings = [
		'1. Dragonborn: +2 Str and +1 Cha',
		'2. Dwarf: +2 Con, and +2 Str or +1 Wis',
		'3. Elf: +2 Dex, and +1 Int, Wis, or Cha',
		'4. Gnome: +2 Int, and +1 Dex or Con',
		'5. Halfling: +2 Dex, and +1 Cha or Con',
		'6. Half-Elf: +2 Cha and +1 to any two stats',
		'7. Half-Orc: +2 Str and +1 Con',
		'8. Human: +1 to all stats',
		'9. Tiefling: +1 Int and +2 Cha'
		]
	for chunk in race_strings:
		print chunk
	choice = int(raw_input(prompt))
	val = race_choices[choice]
	return val

# simple statprint function that can be called
# at different stages
def print_stats(stats):
	atts = [
	'Strength', 'Dexterity', 'Constitution',
	'Intelligence', 'Wisdom', 'Charisma']
	receipt = zip(atts, stats)
	for chunk in receipt:
		print chunk

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
print 'Base stats:'
print_stats(current_stats)

# might need to revert to base_stats later
base_stats = []
for i in range(len(current_stats)):
	base_stats.append(current_stats[i])

print 'Now choose a race.'
chosen_race = picker()
rolled_instance = chosen_race(current_stats)

bonus = rolled_instance.output()
current_stats = plus(*bonus)

print '\nBase Stats were:'
print_stats(base_stats)
print '\nRacial bonuses applied.'
print 'New stats for your %s:' %rolled_instance.race
print_stats(current_stats)
