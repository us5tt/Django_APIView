from django.urls import path
from . views import ParsView


app_name = "items"


urlpatterns = [
    path('items/', ParsView.as_view()),
    path('items/<int:pk>', ParsView.as_view()),
]

