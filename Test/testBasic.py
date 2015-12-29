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

#Basic
postID = aMan.createPost ('Hello post', 'Post di test')
print ('Posted a post with ID', postID, 'from A')	

notFound = True
while(notFound):
	postList = aMan.getList ()
	if not postList:
		print ('No posts in database')
	else:
		print ('Listing posts')
		for post in postList:
			print ('\t', post['postID'])
			if postID == post['postID']:
				notFound = False
	time.sleep (60)
print ('Post', postID, 'found')

commID = aMan.commentPost(postID, 'this is a comment')
print ('Posted a comment with ID', commID, 'from A')

notFound = True
while(notFound):
	post = aMan.getPostInfo (postID)
	print ('ID\t', post['postID'])
	print ('Title\t', post['title'])
	print ('Comments: ')
	for comment in post['comments']:
		print ('\t', comment['comment'])
		if commID == comment['commID']:
			notFound = False
	time.sleep (60)
print ('Comment', commID, 'found')

postID2 = bMan.createPost ('Hello post 2', 'Post di test2')
print ('Posted a post with ID', postID2, 'from B')	

commID2 = aMan.commentPost(postID, 'this is a comment of B')
print ('Posted a comment with ID', commID2, 'from B')

notFound = True
while(notFound):
	post = aMan.getPostInfo (postID)
	print ('ID\t', post['postID'])
	print ('Title\t', post['title'])
	print ('Comments: ')
	for comment in post['comments']:
		print ('\t', comment['comment'])
		if commID2 == comment['commID']:
			notFound = False
	time.sleep (60)
print ('Comment', commID2, 'found')
