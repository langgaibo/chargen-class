# coding: utf8
# 朗盖博 2015

from sys import exit
import csv
import json

prompt = '>: '

version = '1.8'

class Words(object):
	def novel(self):
		pass
	
	def att_words:(self):
		pass
	
	def mod_words(self):
		pass
	
	# !!!!
	def display_MT(self, modtotal)
		pass
		# modtotal = ???
	
	def error_msg(self):
		pass
	
	def not_a_choice(self):
		pass
	
	def quit(self):
		pass
		# exit(0)
	
class Racelist(object):

    races = {
      1:'human', 
	  2:'dragonborn', 
	  3:'dwarf', 
	  4:'elf', 
	  5:'gnome', 
	  6:'halfling',
	  7:'half_elf',
	  8:'half_orc',
	  9:'tiefling'
    }

    def __init__(self, menu_choice):
        self.menu_choice = menu_choice
	def chosen(self, choice):
        val = Racelist.races.get(choice)
        return val

class Race(object):
	
	def __init__(self, racename)
		self.racename = Racelist.chosen
		pass
	
	# def preface(self):
	#	print 'Race = %s' % self.racename
		# bat = 
	
	# def plus_stats(self): # (self, subrace)??
	#	to_add = []
		
	
	
# wordy functions:
	# def novel():
		# print 'menu'
	# def att_words():
		# a_w = ['stats']
	# def mod_words():
		# m_w = [rjust(8, 'mod:']
	# def display_MT(modtotal):
		# takes and prints modtotal from other module
		# and judges the stats
	# def error_msg():
		# just an error message for all modules
	# def quit():
		# prints a goodbye message
	# This should go in Race class:
	# def off_the_bat(bat):
		# print ' '
		# print bat.center(40, '.')

# race functions all have in common:
	# to_add = [six values for attribute +s]
		# except for subrace-able races!
	# race = 'string racename'
	# bat = 'string describing attributes and joke'
	# off_the_bat(bat) = pretty printing
	# return to_add, race 
# subraces have in common:
	# preface strings with menu and benefits
	# input and ifs determine
		# to_add = [six values for attribute +s]
		# race = 'string racename'
		# quit option
		# else:
			# to_add = not_a_choice()
# half_elf is a special case:
	# race = 'string racename'
	# statdict = {'attribute key':range 0, 5 value}
	# stat1, stat2 = 0
	# bat + off_the_bat
	# sub-menu where 2 consec inputs assign + to stats.
	# series of checks to catch doubling, and correct it
	# ridiculous pretty printing taunts

# other:
	# def not_a_choice():
		# to_add = [0, 0, 0, 0, 0, 0]
		# return to_add
	# def csv_block(block):
		# fo = open("scroll.csv", 'wb')
		# wr = csv.writer(fo, quoting=csv.QUOTE_ALL)
		# for row in block:
			# wr.writerow(row)
		# fo.close()
		# print "\n'scroll.csv' overwritten with latest stats.\n"
	#def json_block(block):
		# f = open("scroll.json", 'wb')
		# chunk = str(json.dumps(block))
		# f.write(chunk)
		# f.close()
		# print "\n'scroll.json' overwritten with latest stats.\n"
	# def do_over():
		# to_add = 'panda'
		# race = 'Not Selected'
		# return to_add, race
		