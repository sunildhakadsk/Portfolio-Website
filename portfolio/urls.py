from django.urls import path
from .views import home_view, skills_view, projects_view, contact_view

urlpatterns = [
    path('', home_view, name='home'),
    path('skills/', skills_view, name='skills'),
    path('projects/', projects_view, name='projects'),
    path('contact/', contact_view, name='contact'),
]
