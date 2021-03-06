#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Killer's Aura"
COST = 4
RARITY = 'U'
DESC = "Your opponent burns a card for each Node you control."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	enemy.burn( len(ply.nodes) )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

