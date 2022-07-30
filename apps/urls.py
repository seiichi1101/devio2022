from django.urls import path
from .views import HomeView, OrganizationHomeView

app_name = 'apps'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('org/<int:org_id>/home/', OrganizationHomeView.as_view(), name='org_home'),
]
