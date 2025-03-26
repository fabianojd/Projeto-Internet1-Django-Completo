from django.urls import path
from . import views
## from ..my_tennis_club.urls import urlpatterns

urlpatterns = [
    path('materiais/', views.materiais, name='materiais'),
    path('materiais/details/<int:codigo>', views.details, name='details'),
]