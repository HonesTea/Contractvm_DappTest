# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import logging

from contractvmd import config, dapp, proto
from contractvmd.chain import message
from datetime import date

logger = logging.getLogger(config.APP_NAME)


class DappTestProto:
	DAPP_CODE = [ 0x01, 0x04 ]
	METHOD_REG = 0x01
	METHOD_EDITPOST = 0x06
	METHOD_DELETEPOST = 0x08
	METHOD_COMMPOST = 0x02
	METHOD_EDITCOMMENT = 0x05
	METHOD_DELETECOMMENT = 0x07
	METHOD_CREATEPOLL = 0x03
	METHOD_DELETEPOLL =0x09
	METHOD_VOTE = 0x04
	METHOD_LIST = [METHOD_REG, METHOD_EDITPOST, METHOD_DELETEPOST, METHOD_COMMPOST, METHOD_EDITCOMMENT, METHOD_DELETECOMMENT, METHOD_CREATEPOLL, METHOD_DELETEPOLL, METHOD_VOTE]


class DappTestMessage (message.Message):
	def post (postID, userID, title, body, comments):
		m = DappTestMessage ()
		m.postID = postID
		m.userID = userID
		m.title = title
		m.body = body
		m.comments = comments
		m.DappCode = DappTestProto.DAPP_CODE
		m.Method = DappTestProto.METHOD_REG
		return m

	def editPost (postID, userID, title, body):
		m = DappTestMessage ()
		m.postID = postID
		m.userID = userID
		m.title = title
		m.body = body
		m.DappCode = DappTestProto.DAPP_CODE
		m.Method = DappTestProto.METHOD_EDITPOST
		return m

	def deletePost (postID, userID):
		m = DappTestMessage ()
		m.postID = postID
		m.userID = userID
		m.DappCode = DappTestProto.DAPP_CODE
		m.Method = DappTestProto.METHOD_DELETEPOST
		return m
	
	def createPoll (title, userID, answers, deadline):
		m = DappTestMessage ()
		m.title = title
		m.userID = userID
		m.answers = answers
		m.deadline = deadline		
		m.DappCode = DappTestProto.DAPP_CODE
		m.Method = DappTestProto.METHOD_CREATEPOLL
		return m

	def deletePoll (pollID, userID):
		m = DappTestMessage ()
		m.pollID = pollID
		m.userID = userID
		m.DappCode = DappTestProto.DAPP_CODE
		m.Method = DappTestProto.METHOD_DELETEPOLL
		return m
	
	def commentPost (postID, userID, comment):
		m = DappTestMessage ()
		m.postID = postID
		m.userID = userID
		m.comment = comment
		m.DappCode = DappTestProto.DAPP_CODE
		m.Method = DappTestProto.METHOD_COMMPOST
		return m

	def editComment (commID, userID, comment):
		m = DappTestMessage ()
		m.commID = commID
		m.userID = userID
		m.comment = comment
		m.DappCode = DappTestProto.DAPP_CODE
		m.Method = DappTestProto.METHOD_EDITCOMMENT
		return m

	def deleteComment (commID, userID):
		m = DappTestMessage ()
		m.commID = commID
		m.userID = userID
		m.DappCode = DappTestProto.DAPP_CODE
		m.Method = DappTestProto.METHOD_DELETECOMMENT
		return m

	def vote (pollID, votedAnswer, votingUser):
		m = DappTestMessage ()
		m.pollID = pollID
		m.votedAnswer = votedAnswer
		m.votingUser = votingUser
		m.DappCode = DappTestProto.DAPP_CODE
		m.Method = DappTestProto.METHOD_VOTE
		return m

	def toJSON (self):
		data = super (DappTestMessage, self).toJSON ()

		if self.Method == DappTestProto.METHOD_REG:
			data['postID'] = self.postID	
			data['userID'] = self.userID
			data['title'] = self.title
			data['body'] = self.body
			data['comments'] = self.comments

		elif self.Method == DappTestProto.METHOD_EDITPOST:
			data['postID'] = self.postID	
			data['userID'] = self.userID
			data['title'] = self.title
			data['body'] = self.body

		elif self.Method == DappTestProto.METHOD_DELETEPOST:
			data['postID'] = self.postID
			data['userID'] = self.userID
	
		elif self.Method == DappTestProto.METHOD_CREATEPOLL:
			data['userID'] = self.userID
			data['title'] = self.title
			data['answers'] = self.answers
			data['deadline'] = self.deadline

		elif self.Method == DappTestProto.METHOD_DELETEPOLL:
			data['pollID'] = self.pollID
			data['userID'] = self.userID

		elif self.Method == DappTestProto.METHOD_COMMPOST:
			data['postID'] = self.postID
			data['userID'] = self.userID
			data['comment'] = self.comment

		elif self.Method == DappTestProto.METHOD_EDITCOMMENT:
			data['commID'] = self.commID
			data['userID'] = self.userID
			data['comment'] = self.comment

		elif self.Method == DappTestProto.METHOD_DELETECOMMENT:
			data['commID'] = self.commID
			data['userID'] = self.userID

		elif self.Method == DappTestProto.METHOD_VOTE:
			data['pollID'] = self.pollID
			data['votedAnswer'] = self.votedAnswer
			data['votingUser'] = self.votingUser

		else:
			return None

		return data


class DappTestCore (dapp.Core):
	def __init__ (self, chain, database):
		database.init ('pollDB', [])
		database.init ('postDB', [])
		super (DappTestCore, self).__init__ (chain, database)
	
	def post (self, postID, userID, title, body, comments):
		self.database.listappend ('postDB', {'postID': postID, 'userID': userID, 'title': title, 'body': body, 'comments': comments})

	def editPost (self, postID, userID, newTitle, newBody):
		msgs = self.database.get ('postDB')
		for post in msgs:
			if (post['postID'] == postID) and (post['userID'] == userID):
				post['title'] = newTitle
				post['body'] = newBody
				self.database.set ('postDB', msgs)

	def deletePost (self, postID, userID):	
		msgs = self.database.get ('postDB')
		for post in msgs:
			if (post['postID'] == postID) and (post['userID'] == userID):	
				msgs.remove(post)
				self.database.set ('postDB', msgs)

	def createPoll (self, pollID, userID, title, answers, deadline):
		answersList = []
		for x in answers.split(','):
			answersList.append({x.strip(): 0})		
		self.database.listappend ('pollDB', {'pollID': pollID, 'userID': userID, 'title': title, 'answers': answersList, 'deadline': deadline, 'votes': []})

	def deletePoll (self, pollID, userID):	
		msgs = self.database.get ('pollDB')
		for poll in msgs:
			if (poll['pollID'] == pollID) and (poll['userID'] == userID):	
				msgs.remove(poll)
				self.database.set ('pollDB', msgs)
	
	def commentPost (self, commID, userID, postID, comment):
		msgs = self.database.get ('postDB')
		for x in msgs:
			if x['postID'] == postID:
				x['comments'].append({'commID':commID, 'userID': userID, 'comment':comment})
				self.database.set ('postDB', msgs)

	def editComment (self, commID, userID, newComment):
		msgs = self.database.get ('postDB')
		for post in msgs:
			for comment in post['comments']:
				if (comment['commID'] == commID) and (comment['userID'] == userID):
					comment['comment'] = newComment
					self.database.set ('postDB', msgs)

	def deleteComment (self, commID, userID):
		msgs = self.database.get ('postDB')
		for post in msgs:
			for comment in post['comments']:
				if (comment['commID'] == commID) and (comment['userID'] == userID):
					post['comments'].remove(comment)
					self.database.set ('postDB', msgs)

	def vote (self, voteID, pollID, votedAnswer, votingUser):
		msgs = self.database.get ('pollDB')
		userAlreadyVoted = False
		for poll in msgs:
			if poll['pollID'] == pollID:
				t = []
				for x in poll['deadline'].split(','):
					t.append(int(x.strip()))	
				deadline = date(t[2],t[1],t[0])
				if deadline > date.today():
					if not poll['votes']:
						for answer in poll['answers']:
							if votedAnswer in answer:
								answer[votedAnswer] +=1
								poll['votes'].append({'voteID':voteID, 'votedAnswer':votedAnswer, 'votingUser':votingUser})
								self.database.set ('pollDB', msgs)
					else:
						for vote in poll['votes']:
							userAlreadyVoted = userAlreadyVoted or (vote['votingUser'] == votingUser)
						if not userAlreadyVoted:
							for answer in poll['answers']:
								if votedAnswer in answer:
									answer[votedAnswer] +=1
									poll['votes'].append({'voteID':voteID, 'votedAnswer':votedAnswer, 'votingUser':votingUser})
									self.database.set ('pollDB', msgs)		
				else :
					print('poll already closed')
			

	def getlist (self):
		return self.database.get ('postDB')

	def getlistPolls (self):
		return self.database.get ('pollDB')

	def getPost (self, postID):
		msgs = self.database.get ('postDB')
		for msg in msgs:
			if msg['postID'] == postID:
				print ('post found')
				return msg
		print ('post not found')
		return []

	def getPollInfo (self, pollID):
		msgs = self.database.get ('pollDB')
		for msg in msgs:
			if msg['pollID'] == pollID:
				print ('poll found')
				return msg
		print ('poll not found')
		return []

	def getUserInfo (self, userID):
		p = []
		pp = []
		c = []
		posts = self.database.get('postDB')
		polls = self.database.get('pollDB')
		for post in posts:
			if post['userID'] == userID:
				p.append(post)
			for comment in post['comments']:
				if comment['userID'] == userID:
					c.append(comment)
		for poll in polls:
			if poll['userID'] == userID:
				pp.append(poll)
		info = {'posts':p, 'polls':pp, 'comments':c}
		return info


class DappTestAPI (dapp.API):
	def __init__ (self, core, dht, api):
		print ("api inizializzate")	
		self.api = api
		rpcmethods = {}

		rpcmethods["post"] = {	
			"call": self.method_post,
			"help": {"args": ["postID", "userID", "title", "body", "comments"], "return": {}}
		}

		rpcmethods["editPost"] = {	
			"call": self.method_editPost,
			"help": {"args": ["postID", "userID", "title", "body"], "return": {}}
		}

		rpcmethods["deletePost"] = {
			"call": self.method_deletePost,
			"help": {"args": ["postID", "userID"], "return": {}}	
		}
	
		rpcmethods["createPoll"] = {	
			"call": self.method_createPoll,
			"help": {"args": ["title", "userID", "answers", "deadline"], "return": {}}
		}

		rpcmethods["deletePoll"] = {
			"call": self.method_deletePoll,
			"help": {"args": ["pollID", "userID"], "return": {}}	
		}

		rpcmethods["commentPost"] = {
			"call": self.method_commentPost,
			"help": {"args": ["postID", "userID", "comment"], "return": {}}	
		}

		rpcmethods["editComment"] = {
			"call": self.method_editComment,
			"help": {"args": ["commID", "userID", "comment"], "return": {}}	
		}

		rpcmethods["deleteComment"] = {
			"call": self.method_deleteComment,
			"help": {"args": ["commID", "userID"], "return": {}}	
		}

		rpcmethods["vote"] = {
			"call": self.method_vote,
			"help": {"args": [ "pollID", "votedAnswer", "votingUser"], "return": {}}	
		}	

		rpcmethods["getlist"] = {
			"call": self.method_getlist,
			"help": {"args": [], "return": {}}
		}

		rpcmethods["getlistPolls"] = {
			"call": self.method_getlistPolls,
			"help": {"args": [], "return": {}}
		}		

		rpcmethods["getPost"] = {
			"call": self.method_getPost,
			"help": {"args": ["postID"], "return": {}}
		}
		
		rpcmethods["getPollInfo"] = {
			"call": self.method_getPollInfo,
			"help": {"args": ["pollID"], "return": {}}
		}

		rpcmethods["getUserInfo"] = {
			"call": self.method_getUserInfo,
			"help": {"args": ["userID"], "return": {}}
		}		
		
		errors = {}

		super (DappTestAPI, self).__init__(core, dht, rpcmethods, errors)

	def method_getlist (self):
		return self.core.getlist ()
	
	def method_getlistPolls (self):
		return self.core.getlistPolls ()
	
	def method_getPost (self, postID):
		return self.core.getPost (postID)
		
	def method_getPollInfo (self, pollID):
		return self.core.getPollInfo (pollID)	
	
	def method_getUserInfo (self, userID):
		return self.core.getUserInfo (userID)

	def method_post (self, postID, userID, title, body, comments):
		msg = DappTestMessage.post (postID, userID, title, body, comments)
		return self.createTransactionResponse (msg)
	
	def method_editPost (self, postID, userID, title, body):
		msg = DappTestMessage.editPost (postID, userID, title, body)
		return self.createTransactionResponse (msg)

	def method_deletePost (self, postID, userID):
		msg = DappTestMessage.deletePost (postID, userID)
		return self.createTransactionResponse (msg)

	def method_createPoll (self, title, userID, answers, deadline):
		msg = DappTestMessage.createPoll (title, userID, answers, deadline)
		return self.createTransactionResponse (msg)

	def method_deletePoll (self, pollID, userID):
		msg = DappTestMessage.deletePoll (pollID, userID)
		return self.createTransactionResponse (msg)
	
	def method_commentPost (self, postID, userID, comment):
		msg = DappTestMessage.commentPost (postID, userID, comment)
		return self.createTransactionResponse (msg)

	def method_editComment (self, commID, userID, comment):
		msg = DappTestMessage.editComment (commID, userID, comment)
		return self.createTransactionResponse (msg)

	def method_deleteComment (self, commID, userID):
		msg = DappTestMessage.deleteComment (commID, userID)
		return self.createTransactionResponse (msg)

	def method_vote (self, pollID, votedAnswer, votingUser):
		msg = DappTestMessage.vote (pollID, votedAnswer, votingUser)
		return self.createTransactionResponse (msg)


class dapptest (dapp.Dapp):
	def __init__ (self, chain, db, dht, apimaster):
		self.core = DappTestCore (chain, db)
		api = DappTestAPI (self.core, dht, apimaster)	
		super (dapptest, self).__init__(DappTestProto.DAPP_CODE, DappTestProto.METHOD_LIST, chain, db, dht, api)
		
	def handleMessage (self, m):
		if m.Method == DappTestProto.METHOD_REG:
			logger.pluginfo ('Found new message %s', m.Hash)
			print ("[Dapptest] found a post")
			self.core.post (m.Hash, m.Data['userID'], m.Data['title'], m.Data['body'], m.Data['comments'])

		elif m.Method == DappTestProto.METHOD_EDITPOST:
			logger.pluginfo ('Found new message %s', m.Hash)
			print ("[Dapptest] found an edit for a post")
			self.core.editPost (m.Data['postID'], m.Data['userID'], m.Data['title'], m.Data['body'])

		elif m.Method == DappTestProto.METHOD_DELETEPOST:
			print ("[Dapptest] found a delete for a post")
			logger.pluginfo ('Found new message %s', m.Hash)
			self.core.deletePost (m.Data['postID'], m.Data['userID'])	

		elif m.Method == DappTestProto.METHOD_COMMPOST:
			print ("[Dapptest] found a comment")
			logger.pluginfo ('Found new message %s', m.Hash)
			self.core.commentPost (m.Hash, m.Data['userID'], m.Data['postID'], m.Data['comment'])
		
		elif m.Method == DappTestProto.METHOD_EDITCOMMENT:
			print ("[Dapptest] found an edit for a comment")
			logger.pluginfo ('Found new message %s', m.Hash)
			self.core.editComment (m.Data['commID'], m.Data['userID'], m.Data['comment'])

		elif m.Method == DappTestProto.METHOD_DELETECOMMENT:
			print ("[Dapptest] found a delete for a comment")
			logger.pluginfo ('Found new message %s', m.Hash)
			self.core.deleteComment (m.Data['commID'], m.Data['userID'])			

		elif m.Method == DappTestProto.METHOD_CREATEPOLL:
			logger.pluginfo ('Found new message %s', m.Hash)
			print ("[Dapptest] found a poll")
			self.core.createPoll (m.Hash, m.Data['userID'], m.Data['title'], m.Data['answers'], m.Data['deadline'])
	
		elif m.Method == DappTestProto.METHOD_DELETEPOLL:
			print ("[Dapptest] found a delete for a poll")
			logger.pluginfo ('Found new message %s', m.Hash)
			self.core.deletePoll (m.Data['pollID'], m.Data['userID'])

		elif m.Method == DappTestProto.METHOD_VOTE:
			print ("[Dapptest] found a vote")
			logger.pluginfo ('Found new message %s', m.Hash)
			self.core.vote (m.Hash, m.Data['pollID'], m.Data['votedAnswer'], m.Data['votingUser'])
