from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('index/',views.index),
    path('',views.index),
    path('home/',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('signup/',views.signup),
    path('signin/',views.signin),
    path('gallery/',views.gallery),
    path('assignment/',views.assignment),
    path('logout/',views.logout),

#################################################################
    path('assignmentdetails/',views.assignmentdetails),
    #################################################
    path('profile/', views.profile),
    ###########################################
    path('lecture/', views.lectures),
    path('lcategory/', views.lcategory),
    path('viewlecture/', views.viewlecture),

]