from django.conf.urls import patterns, include, url

urlpatterns = patterns('ripple.views',
	url(r'^rippleView/(?P<pk>\d+)/$','rippleView',name='rippleView')
)