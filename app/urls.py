from django.urls import path
from .views import home, Voting

urlpatterns = [ 
    path('', home, name='home'),
    path('vote',Voting, name="vote"),
]

