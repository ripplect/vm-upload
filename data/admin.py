from django.contrib import admin
from .models import TempUserQueries,UserQueries,UserQueryComments,\
					TempUserOpinions,UserOpinions,UserOpinionLikes, \
					UserOpinionDislike,UserOpinionIrrelevant,\
					UserTags,UserQueryTagMapping,UserOpinionTagMapping


admin.site.register(TempUserQueries)
admin.site.register(UserQueries)
admin.site.register(UserQueryComments)
admin.site.register(TempUserOpinions)
admin.site.register(UserOpinions)
admin.site.register(UserOpinionLikes)
admin.site.register(UserOpinionDislike)
admin.site.register(UserOpinionIrrelevant)
admin.site.register(UserTags)
admin.site.register(UserQueryTagMapping)
admin.site.register(UserOpinionTagMapping)
