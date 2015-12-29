#!/usr/bin/python3
# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
from libcontractvm import Wallet, WalletExplorer, ConsensusManager
from dapptest import DappTestManager
import sys
import time

consMan = ConsensusManager.ConsensusManager ()
consMan.bootstrap ("http://127.0.0.1:8181")

wallet1 = WalletExplorer.WalletExplorer (wallet_file='test.wallet')
wallet2 = WalletExplorer.WalletExplorer (wallet_file='test2.wallet')
aMan = DappTestManager.DappTestManager (consMan, wallet=wallet1)
bMan = DappTestManager.DappTestManager (consMan, wallet=wallet2)

#Advanced
pollID = aMan.createPoll('Titile','answer1, answer2', '1,1,3000')
print ('Posted a poll with ID', pollID, "from A")

notFound = True
while(notFound):
	pollList = aMan.getListPolls ()
	if not pollList:
		print ('No poll in database')
	else:	
		print ('Listing polls')
		for poll in pollList:
			print ('\t', poll['pollID'])
			if pollID == poll['pollID']:
				notFound = False
	time.sleep (60)
print ('Poll', pollID, 'found')

voteID1 = aMan.vote (pollID, 'answer1')
print ('Posted a vote with ID', voteID1, "from A")

voteID2 = aMan.vote (pollID, 'answer2')
print ('Posted a vote with ID', voteID2, "from A")

notFound = True
while(notFound):
	poll = aMan.getPollInfo (pollID)
	print ('ID\t', poll['pollID'])
	for voting in poll['votes']: 
		print ('Votes: ')
		print ('\t', voting['voteID'])
		if voting['voteID']==voteID1:
			notFound = False
	time.sleep (60)
print ('Poll vote', voteID1, 'found')

voteID3 = bMan.vote (pollID, 'answer2')
print ('Posted a vote with ID', voteID3, "from B")

notFound = True
while(notFound):
	poll = aMan.getPollInfo (pollID)
	print ('ID\t', poll['pollID'])
	for voting in poll['votes']: 
		print ('Votes: ')
		print ('\t', voting['voteID'])
		if voting['voteID']==voteID3:
			notFound = False
	time.sleep (60)
print ('Poll vote', voteID3, 'found')

pollID2 = bMan.createPoll('Titile','answer1, answer2', '1,1,3000')
print ('Posted a poll with ID', pollID2, "from B")

notFound = True
while(notFound):
	pollList = aMan.getListPolls ()
	if not pollList:
		print ('No poll in database')
	else:	
		print ('Listing polls')
		for poll in pollList:
			print ('\t', poll['pollID'])
			if pollID2 == poll['pollID']:
				notFound = False
	time.sleep (60)
print ('Poll', pollID2, 'found')

