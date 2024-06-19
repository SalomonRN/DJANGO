from django.urls import path
from .views import first_view, gmail_view

app_name = "publications"

urlpatterns = [
    path('', first_view,),
    path('gmail/', gmail_view)
]
