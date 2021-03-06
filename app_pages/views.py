from django.shortcuts import render
from django.core.paginator import Paginator

from app_listings.models import Listing


def index(request):
    # GET classrooms from datbase ordered by Title
    listings = Listing.objects.order_by('title')

    # Display only 6 classrooms per page
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'pages/index.html', context)
