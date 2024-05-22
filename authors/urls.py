from django.urls import path  # type: ignore # noqa: F401
from . import views


app_name = "authors"

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('register/create/', views.register_create, name='register_create'),
    path('login/', views.login_view, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/news/new/',
         views.dashboard_news_new,
         name='dashboard_news_new'),
    path('dashboard/news/delete/',
         views.dashboard_news_delete,
         name='dashboard_news_delete'),
    path('dashboard/news/<int:id>/edit/',
         views.dashboard_news_edit,
         name='dashboard_news_edit'),
]
