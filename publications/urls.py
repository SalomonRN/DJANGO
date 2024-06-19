from django.urls import path
from .views import first_view, gmail_view

app_name = "publications"

urlpatterns = [
    path('accounts/profile/', dashboard),
    path('gmail/', first_view)
]
