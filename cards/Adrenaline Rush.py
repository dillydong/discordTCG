#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Adrenaline Rush"
COST = 2
RARITY = 'U'
DESC = "Spawn an Adrenaline Node."
TARGETS = None
TYPE = "NodeGen"

#What happens when you play it
def playFunc(ply, enemy, target):
	ply.addNode( 'Adrenaline' )
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

