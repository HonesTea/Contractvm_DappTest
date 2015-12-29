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

#Expert
x = aMan.getUserInfo(aMan.wallet.getAddress())
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

bMan.editComment(commID, 'New comment 1 message')
aMan.editComment(commID, 'New comment 2 message')
bMan.editPost (postID, 'New hello post', 'New message!')
aMan.editPost (postID, 'New hello post A', 'New message!')

notFound = True
while(notFound):
	postList = aMan.getList ()
	if not postList:
		print ('No posts in database')
	else:
		print ('Listing posts')
		for post in postList:
			print ('\t', post['postID'])
			if 'New hello post A' == post['title']:
				notFound = False
	time.sleep (60)
print ('Edited Post ', postID, 'found')

aMan.deleteComment(commID)
commID3 = bMan.commentPost (postID, 'this is a new comment')
print ('Posted a comment with ID', commID3, 'from B')

notFound = True
while(notFound):
	post = aMan.getPostInfo (postID)
	print ('ID\t', post['postID'])
	print ('Title\t', post['title'])
	print ('Comments: ')
	for comment in post['comments']:
		print ('\t', comment['comment'])
		if commID3 == comment['commID']:
			notFound = False
	time.sleep (60)
print ('Comment', commID3, 'found')

aMan.deleteComment (commID3)
bMan.deleteComment (commID3)

found = True
while(found):
	post = aMan.getPostInfo (postID)
	found = False
	print ('ID\t', post['postID'])
	print ('Title\t', post['title'])
	print ('Comments: ')
	for comment in post['comments']:
		print ('\t', comment['commID'])
		if commID3 == comment['commID']:
			found = True
	time.sleep (60)
print ('Comment', commID3, 'deleted')

bMan.deletePost (postID)
aMan.deletePost (postID)

found = True
while(found):
	postList = aMan.getList ()
	found = False

	if not postList:
		print ('No posts in database')
	else:
		print('Listing posts:')
		for post in postList:
			print(post['postID'])
			if postID == post['postID']:
				found = True
	time.sleep (60)
print ('Post', postID, 'deleted')

bMan.deletePoll (pollID2)

found = True
while(found):
	pollList = bMan.getListPolls ()
	found = False
	if not pollList:
		print ('No poll in database')
	else:
		print ('Listing polls:')
		for poll in pollList:
			print (poll['pollID'])
			if pollID2 == poll['pollID']:
				found = True
	time.sleep (60)
print ('Poll', pollID2, 'deleted')

x = aMan.getUserInfo(aMan.wallet.getAddress())
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

x = aMan.getUserInfo(bMan.wallet.getAddress())
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
