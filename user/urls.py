
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('create/',create,name='create'),
    path('delete/<int:id>/',delete,name='delete'),
    path('profile/<int:id>/',profile_see,name='profile'),
    path('update/<int:id>/',profile_update,name='update'),
]