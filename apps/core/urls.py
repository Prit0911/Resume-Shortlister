from django.urls import path, include

urlpatterns = [
    path('', include('apps.accounts.urls')),
    path('', include('apps.jobs.urls')),
    path('', include('apps.skills.urls')),
    path('', include('apps.ranking.urls')),
    path('', include('apps.resumes.urls')),
]


