from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('create/',create,name='create'),
    path('profile/<int:id>/',profile_see,name='profile'),
    path('update/<int:id>/',profile_update,name='update'),
    path('delete/<int:id>/',delete,name='delete'),
    path('inactive_profiles/',delete_profiles,name='inactive_profile'),
    path('delete_permanent/<int:id>/',delete_permanent,name='delete_permanent'),
    path('restore_profiles/<int:id>/',restore_profiles,name='active_profiles'),
]