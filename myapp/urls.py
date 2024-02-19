from django.urls import path
from . import views


#URL cinfiguration
urlpatterns = [
    path('index/', views.index)
]