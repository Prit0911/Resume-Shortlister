from django.urls import path, include
from . import views

urlpatterns = [
    path('skills/', views.SkillsView.as_view(), name='skills'),
]