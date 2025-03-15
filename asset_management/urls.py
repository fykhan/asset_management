from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/', views.user_login, name='user_login'),
    path('assigned-assets/', views.assigned_assets, name='assigned_assets'),
    path('asset-details/<int:barcode>/', views.asset_details, name='asset_details'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('logout/', LogoutView.as_view(next_page='user_login'), name='logout'),
]