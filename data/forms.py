from django.forms import ModelForm
from .models import UserQueries, UserOpinions, TempUserQueries , TempUserOpinions


class UserQueryForm(ModelForm):
	class Meta:
		model = TempUserQueries
		exclude= ['queryOwner','comment']
			


class createQueryOpinion1(ModelForm):
	class Meta:
		model = TempUserOpinions
		exclude= ['opinionOwner','questionOfOpinion','comment']

class createQueryOpinion2(ModelForm):
	class Meta:
		model = TempUserOpinions
		exclude= ['opinionOwner','questionOfOpinion','comment']

class UserOpinionFormWithoutOwner(ModelForm):
	class Meta:
		model = UserOpinions
		exclude= ['opinionOwner','questionOfOpinion','comment']


class UserOpinionFormWithoutQuery(ModelForm):
	class Meta:
		model = UserOpinions
		exclude= ['questionOfOpinion','comment']


