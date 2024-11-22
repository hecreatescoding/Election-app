from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name ="index" ),
    path('login', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout', views.logout_user, name='logout'),
    path('get-manifesto', views.get_manifesto, name='get_manifesto'),
    path('voter_portal', views.voter_portal, name='voter_portal'),  # Voter portal URL

]
