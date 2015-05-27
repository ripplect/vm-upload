from data.models import UserQueries, UserOpinions

""" Query object with opinions """
class UserQueryWithDetails(object):
	def __init__(self,query,opinionList):
		self.query = query 
		self.opinionList = opinionList
		self.OpinionAddButton = True
	def setOpinionAddButton(self,FlagForNewOpinion):
		self.OpinionAddButton = FlagForNewOpinion

""" This method will verify if a user is allowed to add an option or not"""
def isPermittedToAddOpinion(query,opUser):
	""" Some validity check/Exception Handling """
	opList = UserOpinions.objects.filter(questionOfOpinion=query , opinionOwner=opUser)
	opinionCount = opList.count()
	print opinionCount
	print "opinion User = {0}".format(opUser)
	print "query Creator User = {0}".format(query.queryOwner)
	if opUser == query.queryOwner :
		""" Allowing 2 opinions for a query starter"""
		if opinionCount >= 0 and opinionCount < 2: 
			return True
	else :
		""" allow only 1 opinion otherwise """
		if opinionCount == 0 : 
			return True
	return False


