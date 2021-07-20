from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio_details, name='portfolio'),
    path('contact/', views.contact_view, name='contact'),
    path('submit/', views.contact_view, name='submit'),
    path('sentry-debug/', views.trigger_error),
]
