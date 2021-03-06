from django.urls import path
from . import views


urlpatterns = [
    # anything with 'listings/listing_id' will lead to 'listing' method in views.py of app_listings
    path('<int:listing_id>', views.listing, name='listing'),
]
