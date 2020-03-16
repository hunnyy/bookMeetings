from django.urls import path, include
# django.conf.urls import url
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('HrLogin', views.HrLoginView)
router.register('Compadd', views.Addcompview)
router.register('EventAdd', views.EventAddView)



#urlpatterns = [
 #   path('templates/', views.addcomp, name='Addcomp
#    	]

urlpatterns = [

	#url(r'^addcomp/$', views.addcomp, name='Addcomp'),
	#url(r'^compadd/$', views.compadd, name='Compadd'),
	#path('',login_page),
	#path('',register_page),
	path('', include(router.urls))


]