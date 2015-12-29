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

userID = input ('insert ID of the user: ')

while True:
	os.system ('clear')
	print ('Reading info:')
	x = dtMan.getUserInfo (userID)

	print ('Listing posts: ')
	for post in x['posts']:
		print ('ID\t', post['postID'])
		print ('Title\t', post['title'])

	print ('Listing comments: ')
	for comment in x['comments']:
		print ('ID\t', comment['commID'])
		print ('Text\t', comment['comment'])

	print ('Listing polls: ')
	for poll in x['polls']:
		print ('ID\t', poll['pollID'])
		print ('Title\t', poll['title'])
	time.sleep (5)
