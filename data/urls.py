from django.conf.urls import patterns, include, url


urlpatterns = patterns('data.views',
	url(r'^newquery$','newQuery',name='newQuery'),
	url(r'^newOpinion/(?P<qid>\d+)/$','newOpinion',name='newOpinion')
)

