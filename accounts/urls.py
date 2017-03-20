from django.conf.urls import include, url,patterns
#from accounts.views import register,login,create_user
from django.contrib import admin

urlpatterns =(
        url(r'^admin/', include(admin.site.urls)),
        #'accounts.views',
        #url(r'^register/$','register'),
        #url(r'^login/$','login'),
        #url(r'^create_user/$','create_user'),
        #url(r'^accounts/login_user/$','login_user'),
)
