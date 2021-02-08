from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',views.homeView, name="home"),
    path('projects/', views.ProjectHome.as_view(), name="projects"),
    path('projects/<slug:slug>/', views.ProjectDetail.as_view(), name="project-detail"),
    path('blog/', views.BlogHome.as_view(), name="blog"),
    path('blog/<slug:slug>/', views.BlogDetail.as_view(), name="blog-detail")
]
