from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import LoginCheck, HomePage , CreateNote , DeleteNote , UpdateNote , DetailNote 
from . import views
urlpatterns = [
    path('',LoginCheck.as_view(),name="signin"),
    path('Home/',HomePage.as_view(),name="homepage"),
    path('NewNote/',CreateNote.as_view(),name="createnote"),
    path('Confirm/<int:pk>',DeleteNote.as_view(),name="deletenote"),
    path('UpdateMyNote/<int:pk>',UpdateNote.as_view(),name="updatenote"),
    path('MyNote/<int:pk>/',DetailNote.as_view(),name="shownote"),
    path('CreateAccount', views.sign_up ,name='signup'),
    path('logout/',LogoutView.as_view(next_page='signin'),name='logout')
]
