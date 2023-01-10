from django.urls import path

from .views.immobile_views import ImmobileViews
from .views.ad_views import AdViews
from .views.reservation_views import ReservationViews

urlpatterns = [
    path('immobiles', ImmobileViews.as_view({'get': 'list', 'post': 'create'}), name="immobiles"),
    path('immobiles/<int:pk>', ImmobileViews.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name="immobile"),
    path('ads', AdViews.as_view({'get': 'list', 'post': 'create'}), name="ads"),
    path('ads/<int:pk>', AdViews.as_view({'get': 'retrieve', 'put': 'update'}),
         name="ad"),
    path('reservations', ReservationViews.as_view({'get': 'list', 'post': 'create'}), name="reservations"),
    path('reservations/<int:pk>', ReservationViews.as_view({'get': 'retrieve', 'delete': 'destroy'}),
         name="reservation"),

]
