from django.urls import path
from member import views

urlpatterns = [
    path('', views.show_ch2, name='enter_staff2'),
]