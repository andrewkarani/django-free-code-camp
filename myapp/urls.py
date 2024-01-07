from django.urls import path
from . import views # here we r importing views.py file

urlpatterns = [ # this is a list which will take all the urls we have in our project
    path('', views.index, name='index'),# the empty quotes imply home page/ main site/project
    # the urls are py files. 
    # the views,index indicates everything that happens wen a user comes to this particular url. we may render a html file
    # but b4 we can use that views we need import it
    # the views.index the index reps a function. it will go to the views file and look for the function called index
    # watever is done in the index function is what is going to be assigned in this partic ular url
    # it is advisable to name it the same thing you named the function. it is like a kind of id
    
    #creating the url for the action of the html file 
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'), # we need to create the functionnamed login
    path ('logout', views.logout, name='logout'),
    path('post/str:pk', views.post, name='post')# means our website url slash post slash  a string and we are naming that string pk
]
