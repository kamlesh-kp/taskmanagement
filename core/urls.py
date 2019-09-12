from django.urls import path
from .views import User_SignupList,User_SignupDetail

urlpatterns = [
    path('user/', User_SignupList.as_view()),
    path('user/<int:pk>',User_SignupDetail.as_view())
]