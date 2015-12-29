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

while True:
	os.system ('clear')
	print ('List of polls:')
	v = dtMan.getListPolls ()
	
	if not v:
		print ('No polls in database')
	else:
		for x in v:
			print ('Poll ID')
			print ('\t',x['pollID'])
			print ('Poll title')
			print ('\t',x['title'])
	time.sleep (5)
