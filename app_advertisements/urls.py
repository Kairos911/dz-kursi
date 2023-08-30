from django.urls import path
from .views import advetisements_detail, index, top_sellers, advertisement_post

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisement_post, name="adv-post"),
    path('advertisement/<int:pk>', advetisements_detail, name="adv-detail"  )
]
