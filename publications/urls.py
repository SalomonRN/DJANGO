from django.urls import path
from .views import first_view, gmail_view, dashboard

app_name = "publications"

urlpatterns = [
    path('accounts/profile/', dashboard),
    path('gmail/', gmail_view)
]
