from django.conf.urls import include, url
from django.contrib import admin
from blog.views import *
from blog.models import Photo


import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),

    url(r'^media/(?P<path>.*)','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),

    #url(r'^te/$', te),
    #url(r'^blog/css/(?P<path>.*)', 'django.views.static.serve',
    #{'document_root': settings.CSS_DIR}),
    #url(r'^blog/image/(?P<path>.*)', 'django.views.static.serve',
    #{'document_root': settings.IMAGE_DIR}),
    #url(r'^blog/js/(?P<path>.*)', 'django.views.static.serve',
    #{'document_root': settings.JS_DIR}),

]
