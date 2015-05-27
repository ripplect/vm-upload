from django.contrib.auth.models import User
from django.db import models

class QueryManager(models.Manager):
	def queriesForUser(self,user):
		""" return a list of questions for a particular user"""
		return super(QueryManager,self).get_queryset().filter(queryOwner_id=user.id)

class TempUserQueries(models.Model):
	queryOwner = models.ForeignKey(User)
	question = models.CharField(max_length=64)
	timeStamp = models.DateTimeField(auto_now_add=True)
	comment = models.CharField(max_length=128,blank=True)
	
	objects = QueryManager()
	
	def __str__(self):
		return "{0} ?".format(self.question)
		"""return "<{0}> {1} ?".format(self.queryOwner.first_name,self.question)"""

class UserQueries(models.Model):
	queryOwner = models.ForeignKey(User, related_name="userQueryOwner")
	question = models.CharField(max_length=64)
	timeStamp = models.DateTimeField(auto_now_add=True)
	comment = models.CharField(max_length=128,blank=True)
	
	objects = QueryManager()
	
	def __str__(self):
		return "{0} ?".format(self.question)
		"""return "<{0}> {1} ?".format(self.queryOwner.first_name,self.question)"""

	def setUserQueriesFromTemp(self,tempUserQueries):
		self.queryOwner = tempUserQueries.queryOwner
		self.question = tempUserQueries.question
		self.comment = tempUserQueries.comment







class UserQueryComments(models.Model):
	question = models.ForeignKey(UserQueries)
	commentOwner = models.ForeignKey(User)
	timeStamp = models.DateTimeField(auto_now_add=True)
	commentText = models.CharField(max_length=128,blank=True)


class OpinionManager(models.Manager):
	def opinionsForQuery(self,UserQueries):
		""" returns the list of opinions registered for a particular query """
		return super(OpinionManager,self).get_queryset().filter(questionOfOpinion_id=UserQueries.id)

class TempUserOpinions(models.Model):
	opinionOwner = models.ForeignKey(User)
	questionOfOpinion = models.ForeignKey(TempUserQueries)
	opinion = models.CharField(max_length=64)
	timeStamp = models.DateTimeField(auto_now_add=True)
	comment = models.CharField(max_length=128,blank=True)

	objects = OpinionManager()

	def __str__(self):
		return "<{0}> {1}".format(self.opinionOwner.first_name,self.opinion)

class UserOpinions(models.Model):
	opinionOwner = models.ForeignKey(User, related_name="userOpinionOwner")
	questionOfOpinion = models.ForeignKey(UserQueries,related_name="parentUserQuery")
	opinion = models.CharField(max_length=64)
	timeStamp = models.DateTimeField(auto_now_add=True)
	comment = models.CharField(max_length=128,blank=True)

	objects = OpinionManager()

	def __str__(self):
		return "<{0}> {1}".format(self.opinionOwner.first_name,self.opinion)

	def setUserOpinionsFromTemp(self,tempUserOpinions,userQueries):
		self.opinionOwner = tempUserOpinions.opinionOwner
		self.opinion = tempUserOpinions.opinion
		self.comment = tempUserOpinions.comment
		self.questionOfOpinion = userQueries

		


class UserOpinionLikes(models.Model):
	likeUser = models.ForeignKey(User)
	opinionLiked = models.ForeignKey(UserOpinions)
	timeStamp = models.DateTimeField(auto_now_add=True)

class UserOpinionDislike(models.Model):
	dislikeUser = models.ForeignKey(User)
	opinion = models.ForeignKey(UserOpinions)
	timeStamp = models.DateTimeField(auto_now_add=True)

class UserOpinionIrrelevant(models.Model):
	irrelevantUser = models.ForeignKey(User)
	opinion = models.ForeignKey(UserOpinions)
	timeStamp = models.DateTimeField(auto_now_add=True)

class UserTags(models.Model):
	tag = models.CharField(max_length=128)

class UserQueryTagMapping(models.Model):
	tag = models.ForeignKey(UserTags)
	question = models.ForeignKey(UserQueries)

class UserOpinionTagMapping(models.Model):
	tag = models.ForeignKey(UserTags)
	opinion = models.ForeignKey(UserOpinions)
