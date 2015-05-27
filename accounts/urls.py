from django.conf.urls import patterns, include, url


urlpatterns = patterns('accounts.views',
	url(r'^home$','home',name='account_home'),
	url(r'^ripples$', 'ripples' ,name='ripples')
    
)

