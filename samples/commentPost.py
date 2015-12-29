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

wallet = WalletExplorer.WalletExplorer (wallet_file='test.wallet')
dtMan = DappTestManager.DappTestManager (consMan, wallet=wallet)

postId = input ('Insert ID of the post you want to comment: ')
comment = input ('Insert your comment: ')

try:
	print ('tento il broadcast')
	print ('Broadcasted:', dtMan.commentPost (postId, comment))
except:
	print ('Error.')
	
