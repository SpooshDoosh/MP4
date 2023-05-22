from django.urls import path
from .views import RenderHTMLPlayer


urlpatterns = [
    path('/<int>:id', RenderHTMLPlayer.as_view(), name='music-player')
]
