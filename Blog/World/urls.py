from django.contrib import admin
from django.urls import path

from World.views import HomeWorld, WorldByCategory, ViewWorld, AddWorld


urlpatterns = [
    path('', HomeWorld.as_view(), name='world'),
    path('category/<int:category_id>/', WorldByCategory.as_view(), name='categoryworld'),
    path('world/<int:pk>/', ViewWorld.as_view(), name='view_world'),
    path('world/add_world/', AddWorld.as_view(), name='add_world'),

]


