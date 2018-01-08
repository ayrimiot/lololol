#!/usr/bin/env python3
class Player(object):
	def __init__(self, myname='user', myscore=0, lvlmass=0):
		self.myname = myname
		self.myscore = myscore
		self.lvlmass = lvlmass
	def name(self):
		x = str(self.myname)
		return x
	def lvlmass(self, mass):
		x = self.lvlmass
		x = x + mass
		return x
	def lvl(self):
		x = self.myscore
		return x

pl = Player()
pl.name = "Ayrimiot"
pl.lvl = 0
pl.lvlmass = 0

print(pl.lvlmass)
print(pl.lvl)
