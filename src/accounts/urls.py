from django.urls import include, path

from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.UserSignUpView.as_view(), name='user_signup'),
    path('members/', include(([
        path('<slug:slug>/', views.profile, name='home'),
    ], 'members'))),
]