#!/usr/bin/python3
# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
from libcontractvm import Wallet, WalletExplorer, ConsensusManager
from dapptest import DappTestManager
from datetime import date
import sys
import time

consMan = ConsensusManager.ConsensusManager ()
consMan.bootstrap ("http://127.0.0.1:8181")

wallet = WalletExplorer.WalletExplorer (wallet_file='test.wallet')
dtMan = DappTestManager.DappTestManager (consMan, wallet=wallet)

title = input ('Insert your poll title: ')
answers = input ('Insert the answers to your poll: (Answer1, Answer2, etc ) ')

wrong = True
while (wrong):
	print ('Insert deadline: ')
	day = input('day: ')
	month = input('month ')
	year = input('year ')

	deadline = date(int(year), int(month), int(day)) #the date class handle by itself wrong dates like 56 jenuary 1996. Should i try/catch it?

	if date.today() < deadline :
		wrong = False
	else:
		print ('the date you insert is already past')

deadline = day + ',' + month + ',' + year

try:
	print ('tento il broadcast')
	print ('Broadcasted:', dtMan.createPoll (title, answers, deadline))
except:
	print ('Error.')
