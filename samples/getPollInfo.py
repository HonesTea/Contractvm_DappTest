#!/usr/bin/python3
# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
from libcontractvm import Wallet, WalletExplorer, ConsensusManager
from dapptest import DappTestManager
import sys
import time
import os

consMan = ConsensusManager.ConsensusManager ()
consMan.bootstrap ("http://127.0.0.1:8181")

wallet = WalletExplorer.WalletExplorer (wallet_file='test.wallet')
dtMan = DappTestManager.DappTestManager (consMan, wallet=wallet)

pollID = input ('insert ID of the poll you want to read: ')

while True:
	os.system ('clear')
	print ('Reading post:')
	poll = dtMan.getPollInfo (pollID)
	if not poll:
		print ('poll not found')
	else:
		print ('Poll ID'), 
		print ('\t', poll['pollID'])
		print ('Poll title')
		print ('\t', poll['title'])
		print ('Poll answers ')
		for answer in poll['answers']:
			print ('\t', answer)
		for voting in poll['votes']: 
			print ('\t', voting)
	time.sleep (5)
