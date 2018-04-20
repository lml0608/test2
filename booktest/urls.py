from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$',views.index,name='index'),
    url(r'^(\d+)$',views.show,name='show'),
    url(r'^index2/$',views.index2,name='index2'),
    url(r'^user1/$',views.user1,name='user1'),
    url(r'^htmlTest/$',views.htmlTest,name='htmlTests'),
    url(r'^csrf1/$', views.csrf1),
    url(r'^csrf2/$', views.csrf2),
]