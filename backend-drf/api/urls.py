from django.urls import path
from accounts import views as UserViews

urlpatterns = [
    path('register/', view=UserViews.RegisterView.as_view()),
]