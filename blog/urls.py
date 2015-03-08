from django.conf.urls import include, url
from blog.views import *
from  django.conf import  settings
#from django.conf.urls.static import static

urlpatterns = [

    url(r'^$', archive),
    url(r'^te/$', te),
    url(r'^contact/$', contact),
    url(r'^message/$', remark),
    url(r'^search/$', search),
    url(r'^media/(?P<path>.*)','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    #url(r'^item/(?P<object_id>\d+)/$','django.views.static.serve',name='item_detail'),
    #url(r'^photos/(?P<object_id>\d+)/$','django.views.static.serve',name='photo_detail'),
    #url(r'^css/(?P<path>.*)', 'django.views.static.serve',
    #{'document_root': settings.CSS_DIR}),
    #url(r'^image/(?P<path>.*)', 'django.views.static.serve',
    #{'document_root': settings.IMAGE_DIR}),
    #url(r'^js/(?P<path>.*)', 'django.views.static.serve',
    #{'document_root': settings.JS_DIR}),
    #url(r'^templates/(?P<path>.*)', 'django.views.static.serve',
    #{'document_root': './blog/templates'}),
]
#urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
#urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )