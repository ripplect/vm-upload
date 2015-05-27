from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import UserQueries , UserOpinions , TempUserQueries , TempUserOpinions
from .forms import UserQueryForm ,createQueryOpinion1 , createQueryOpinion2 , UserOpinionFormWithoutQuery
from . import utils
from ripple import views



@login_required
def newQuery(request):
	if request.method == 'POST':
		tempQuery = TempUserQueries(queryOwner=request.user)
		queryForm = UserQueryForm(request.POST, instance=tempQuery)
		querySaveFlag = False
		opinionSaveFlag1 = False
		opinionSaveFlag2 = False
		if queryForm.is_valid():
			tempQuery = queryForm.save()
			querySaveFlag = True

		tempOp1 = TempUserOpinions(opinionOwner=request.user,questionOfOpinion=tempQuery)
		opinionForm1 = createQueryOpinion1(request.POST, instance=tempOp1)
		if opinionForm1.is_valid():
			opinionForm1.save()
			opinionSaveFlag1 = True

		tempOp2 = TempUserOpinions(opinionOwner=request.user,questionOfOpinion=tempQuery)
		opinionForm2 = createQueryOpinion2(request.POST, instance=tempOp2)
		if opinionForm2.is_valid():
			opinionForm2.save()
			opinionSaveFlag2 = True

		if querySaveFlag and opinionSaveFlag1 and opinionSaveFlag2:
			# need to be inside a transaction
			# create and save user queries and opinions and remove the temp
			query = UserQueries()
			query.setUserQueriesFromTemp(tempQuery)
			query.save()

			opinion1 = UserOpinions()
			opinion1.setUserOpinionsFromTemp(tempOp1,query)
			opinion1.save()

			opinion2 = UserOpinions()
			opinion2.setUserOpinionsFromTemp(tempOp2,query)
			opinion2.save()

			tempQuery.delete()
			tempOp1.delete()
			tempOp2.delete()

			return redirect('account_home')
# to be considered
#		else:
#			tempQuery.delete()
#			tempOp1.delete()
#			tempOp2.delete()


	if request.method == 'GET':
		queryForm = UserQueryForm()
		opinionForm1 = createQueryOpinion1()
		opinionForm2 = createQueryOpinion2()

	context = {'titleName': 'New Ripple', 
				'brandName': request.user.first_name,
				'queryForm': queryForm ,
				'opinionForm1': opinionForm1,
				'opinionForm2': opinionForm2 }
	
	return render(request, "data/new_query_form.html", context)


@login_required
def newOpinion(request,qid):
	query = UserQueries.objects.get(pk=qid)
	if request.method == 'POST':
		opinion = UserOpinions(questionOfOpinion=query)
		if utils.isPermittedToAddOpinion(query,request.user):
			newOpinionForm = UserOpinionFormWithoutQuery(request.POST,instance=opinion)
			if newOpinionForm.is_valid():
				newOpinionForm.save();
#				redirect("{% url 'rippleView' pk=qid %}")
#				return render(request,"ripple/rippleView.html",context)
				return views.rippleView(request,qid)

		else:
#			redirect("{% url 'rippleView' pk=qid %}")
			return views.rippleView(request,qid)
	if request.method == 'GET':
		newOpinionForm = UserOpinionFormWithoutQuery();

	context = {'titleName': 'Add View', 
				'brandName': request.user.first_name,
				'newOpinionForm': newOpinionForm,
				'queryId':qid }
	return render(request,'data/new_option_form.html',context)

