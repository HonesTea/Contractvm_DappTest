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

postID = input ('insert ID of the post you want to read: ')

while True:
	os.system ('clear')
	print ('Reading post:')
	x = dtMan.getPostInfo (postID)
	print ('Post ID')
	print ('\t',x['postID'])
	print ('Post title')
	print ('\t', x['title'])
	print ('Post message')
	print ('\t', x['body'])
	print ('Post comments: ')
	for comment in x['comments']:
		if "b0fff9801027db6a0bd923c63de0b35f5610b73a2e0ec22858105badb033e398" == comment['commID']:
			print ('founded')
		print ('\tComment ID')
		print ('\t', comment['commID'])
		print ('\tComment text')
		print ('\t', comment['comment'])
	time.sleep (5)
