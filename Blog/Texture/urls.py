from django.contrib import admin
from django.urls import path

from Texture.views import HomeTexture, TextureByCategory, ViewTexture, AddTexture


urlpatterns = [
    path('', HomeTexture.as_view(), name='texture'),
    path('category/<int:category_id>/', TextureByCategory.as_view(), name='categorytexture'),
    path('texture/<int:pk>/', ViewTexture.as_view(), name='view_texture'),
    path('texture/add_texture/', AddTexture.as_view(), name='add_texture'),

]

