from django.urls import path
from .views import first_view

app_name = "publications"

urlpatterns = [
    path("api/", first_view,),
    # path('', )
]
