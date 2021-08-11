from django.urls import path
from .views import corona_case_home_view

urlpatterns = [
    path('india/',corona_case_home_view),
]
