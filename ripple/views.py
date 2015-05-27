from django.shortcuts import render , redirect , get_object_or_404

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from data.models import UserQueries , UserOpinions 
from data import utils
from data.utils import UserQueryWithDetails


@login_required
def rippleView(request,pk):
	rippleQuery = get_object_or_404(UserQueries,pk=pk)
	OpinionButtonFlag = False

#	return render(request,'accounts/home.html')
	if request.method == 'POST':
		# do something
		return render(request,'accounts/home.html')

	if request.method == 'GET':
		#render the query with details.
		rippleQueryOpinionList = UserOpinions.objects.opinionsForQuery(rippleQuery)
		queryWithDetails = UserQueryWithDetails(rippleQuery,rippleQueryOpinionList)

		if utils.isPermittedToAddOpinion(rippleQuery,request.user):
			OpinionButtonFlag = True

		context = {'titleName': 'Ripplect', 
				'brandName': request.user.first_name,
				'queryWithDetails': queryWithDetails,
				'OpinionButtonFlag': OpinionButtonFlag }
		return render(request,"ripple/rippleView.html",context)


