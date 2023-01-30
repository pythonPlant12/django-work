from django.urls import path
from . import views

urlpatterns = [
    # To create a url with no difference of name of url path in challenges app
    # in <month> we can put another name, <> means that it can be whatever)
    # This name should go as a parameter in views.py function 
    # We can also sort path by its type like int or str
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")

]