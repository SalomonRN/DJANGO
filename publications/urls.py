from django.urls import path
from .views import first_view, gmail_view

app_name = "publications"

urlpatterns = [
    path('', gmail_view),
    path('gmail/', first_view)
]
