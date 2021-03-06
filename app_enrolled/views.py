from django.shortcuts import redirect
from django.contrib import messages

from .models import Enrolled


def enroll(request):
    if request.method == 'POST':
        # Get form values from listing.html
        class_id = request.POST['class_id']
        listing_title = request.POST['class_title']
        user_id = request.POST['student_id']
        student_name = request.POST['student_name']
        student_email = request.POST['student_email']

        # Check if the logged in student has already enrolled
        if request.user.is_authenticated:
            user_id = request.user.id
            has_enrolled = Enrolled.objects.all().filter(
                class_title=listing_title, user_id=user_id)
            if has_enrolled:
                messages.error(
                    request, 'You have already enrolled for this class')
                return redirect('/listing/' + class_id)

        contact = Enrolled(
            class_id=class_id,
            class_title=listing_title,
            user_id=user_id,
            student_name=student_name,
            student_email=student_email,
        )

        contact.save()

        messages.success(
            request, f'Successfully Enrolled for {listing_title} class.')

        return redirect('/listing/' + class_id)
