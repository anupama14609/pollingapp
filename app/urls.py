from django.urls import path
from .views import Sortdata, home, Voting

urlpatterns = [ 
    path('', home, name='home'),
    path('vote',Voting, name="vote"),
    path('sort', Sortdata, name='sort'),
]

