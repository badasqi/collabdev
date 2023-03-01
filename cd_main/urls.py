from django.urls import path
from .views import *


urlpatterns = {
    path('', home),
    path('project/', project),
    path('user/', user),
}