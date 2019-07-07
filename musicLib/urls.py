from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('songs', views.SongView)
router.register('albums', views.AlbumView)
router.register('artists', views.ArtistView)

urlpatterns = [
    path('', include(router.urls))
]
