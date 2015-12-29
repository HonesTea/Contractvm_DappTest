# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from libcontractvm import Wallet, ConsensusManager, DappManager

class DappTestManager (DappManager.DappManager):
	def __init__ (self, consensusManager, wallet = None):
		super (DappTestManager, self).__init__(consensusManager, wallet)

	def createPost (self, title, body):
		cid = self.produceTransaction ('dapptest.post', [0, self.wallet.getAddress(), title, body, []])
		return cid
	
	def editPost (self, postID, title, body):
		cid = self.produceTransaction ('dapptest.editPost', [postID, self.wallet.getAddress(), title, body])
		return cid
	
	def deletePost (self, postID):
		cid = self.produceTransaction ('dapptest.deletePost', [postID, self.wallet.getAddress()])
		return cid

	def commentPost (self, postID, comment):
		cid = self.produceTransaction ('dapptest.commentPost', [postID, self.wallet.getAddress(), comment])
		return cid

	def editComment (self, commID, comment):
		cid = self.produceTransaction ('dapptest.editComment', [commID, self.wallet.getAddress(), comment])
		return cid

	def deleteComment (self, commID):
		cid = self.produceTransaction ('dapptest.deleteComment', [commID, self.wallet.getAddress()])
		return cid

	def createPoll (self, title, answers, deadline):
		cid = self.produceTransaction ('dapptest.createPoll', [title, self.wallet.getAddress(), answers, deadline])
		return cid

	def deletePoll (self, pollID):
		cid = self.produceTransaction ('dapptest.deletePoll', [pollID, self.wallet.getAddress()])
		return cid

	def vote (self, pollID, votedAnswer):
		cid = self.produceTransaction ('dapptest.vote', [pollID, votedAnswer, self.wallet.getAddress()])
		return cid

	def getList (self):
		return self.consensusManager.jsonConsensusCall ('dapptest.getlist', [])['result']
	
	def getListPolls (self):
		return self.consensusManager.jsonConsensusCall ('dapptest.getlistPolls', [])['result']	

	def getPostInfo (self, postID):
		return self.consensusManager.jsonConsensusCall ('dapptest.getPost', [postID])['result']
	
	def getPollInfo (self, pollID):
		return self.consensusManager.jsonConsensusCall ('dapptest.getPollInfo', [pollID])['result']

	def getUserInfo (self, userID):
		return self.consensusManager.jsonConsensusCall ('dapptest.getUserInfo', [userID])['result']
	
	
