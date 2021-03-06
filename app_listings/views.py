from django.shortcuts import render, get_object_or_404

from .models import Listing


def listing(request, listing_id):
    # get_object_or_404 -> Fetch the object values or 404 page if doesn't exist
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)
