from django.urls import path
from . import views 
# import views to access created views method for /january url, # connect challenges app to main project , go to main urls.py                             
urlpatterns =[
    path("",views.index),
    path("<int:month>",views.monthly_challenge_by_number),
    path("<str:month>",views.monthly_challenge,name="month-challenge"),
    

]