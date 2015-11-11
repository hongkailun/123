from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.conf.urls import patterns, include, url
from django.contrib import admin
from books.views import *
from mysite import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hello/$',hello),
    url(r'^index/$',index),
    url(r'^add/$',add),
    url(r'^addauthor/$',addauthor),
    url(r'^add_Successed/$',add_Successed),
    url(r'^search_again/$', search_again),
    url(r'^updata/$',updata),
    url(r'^updata_Successed/$',updata_Successed),
    url(r'^detailedbook/$',detailedbook),
    url(r'^delete/$',delete),
    url(r'^search-form/$', search_form),
    url(r'^search/$', search),
    url(r'^show/$', show),
    (r'^Media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS,'show_indexes': True}),


    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)