from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from data.models import UserQueries , UserOpinions
from data import utils
from data.utils import UserQueryWithDetails



@login_required
def home(request):
	userQueries = UserQueries.objects.queriesForUser(request.user)

	queriesWithDetails = []
	for q in userQueries:
		oList = UserOpinions.objects.opinionsForQuery(q)
		queryDetailObj = UserQueryWithDetails(q,oList)
		if utils.isPermittedToAddOpinion(q,request.user):
			queryDetailObj.setOpinionAddButton(True)
		else:
			queryDetailObj.setOpinionAddButton(False)
		queriesWithDetails.append(queryDetailObj)

	context = {'titleName': 'Ripplect', 
				'brandName': request.user.first_name,
				'queriesWithDetails': queriesWithDetails}
	return render(request,"accounts/home.html",context)


@login_required
def ripples(request):
	userQueries = UserQueries.objects.all()

	queriesWithDetails = []
	for q in userQueries:
		oList = UserOpinions.objects.opinionsForQuery(q)
		queryDetailObj = UserQueryWithDetails(q,oList)
		if utils.isPermittedToAddOpinion(q,request.user):
			queryDetailObj.setOpinionAddButton(True)
		else:
			queryDetailObj.setOpinionAddButton(False)
		queriesWithDetails.append(queryDetailObj)

	context = {'titleName': 'Ripplect', 
				'brandName': request.user.first_name,
				'queriesWithDetails': queriesWithDetails}
	return render(request,"accounts/ripples.html",context)




