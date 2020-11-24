from django.urls import path
''' 
This is to allow us to connect the PROJECT's  url with this APP's url 
it will then allow us to define paths here as we had included (grams urls)
in the PROJECT.
'''

from . import views
'''
Here we are importing the views as we shall connect templates from there 
'''

from django.conf import settings
'''
This is importing the settings configurations to (gramapp)
'''

from django.conf.urls.static import static
'''
This is to import static-files in urls
'''
from django.shortcuts import render, redirect


'''End Of Import'''
#---------------------------------------------------------------------#

urlpatterns=[

    #Home page url
    path('',views.index, name='index'),

    #Explore page url
    path('explore',views.explore,name ='explore'),

    #The Notification page url
    path('notification',views.notification,name ='notification'),

    #The Profile page url
    path('profile',views.profile,name ='profile'),

    #The Login page url
    path('login',views.login,name ='login'),


    #The Login-Out page url
    path('logout',views.index,{'next_page': 'accounts:login'}, name='logout'),

    #This is the uploading page url
    path('upload',views.upload,name ='upload'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
