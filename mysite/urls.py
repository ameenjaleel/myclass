from django.conf.urls import include, url,patterns
from django.contrib import admin
from django.conf import settings


urlpatterns =[
    # Examples:
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$','accounts.views.login',name="login"),
    url(r'^login_user/$','accounts.views.login_user',name="login_user" ),
    url(r'^register/$','accounts.views.register',name="register"),
    url(r'^create_user/$','accounts.views.create_user',name="create_user"),
    url(r'^logout_user/$','accounts.views.logout_user',name="logout_user"),
    url(r'^home/$','home.views.index',name="index"),
    #url(r'^(?P<classroom_id>[0-9]+)/home/$','home.views.index',name="index"),
    url(r'^classroom/create/$', 'home.views.classroom_create', name='classroom_create'),
    url(r'^(?P<classroom_id>[0-9]+)/myclass/$', 'home.views.myclass', name='myclass'),
    #url(r'^(?P<classroom_id>[0-9]+)/delete_classroom/$', 'home.views.delete_classroom', name='delete_classroom'),
    url(r'^create/(?P<pk>\d+)/student/$', 'home.views.create_student', name='create_student'),
    #url(r'^books/(?P<pk>\d+)/update/$', views.book_update, name='book_update'),
    url(r'^classroom/(?P<pk>\d+)/delete/$', 'home.views.delete_classroom', name='delete_classroom'),
    url(r'^student/(?P<pk>\d+)/delete/$', 'home.views.delete_student', name='delete_student'),

]

#if settings.DEBUG:
#	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
