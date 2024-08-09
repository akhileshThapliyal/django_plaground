from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import path
from iommi.path import register_path_decoding

from .views import ProfileInfoPage

app_name = 'playground'

urlpatterns = [
    path('profile_info', login_required(ProfileInfoPage().as_view()), name='profile_info')
]
