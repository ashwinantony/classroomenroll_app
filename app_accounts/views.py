from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from app_enrolled.models import Enrolled


def register(request):
    if request.method == 'POST':
        # Get form values from register.html
        student_name = request.POST['student_name'].split()
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Password match check
        if password == password2:
            # check if email exist in database
            if User.objects.filter(email=email).exists():
                # Alert Message: email already exist
                messages.error(request, 'Email is already registered')
                return redirect('register')
            else:
                # Register user
                user = User.objects.create_user(
                    username=email,
                    password=password,
                    email=email,
                    first_name=student_name[0],
                    last_name=student_name[-1]
                )

                # Login student right-away after registration - include tag in index.html as well
                # auth.login(request, user)
                # messages.success(
                #     request, 'Successfully registered! You are now logged in'
                # )
                # return redirect('index')

                # Register student and redirect to login page
                user.save()

                # Send Welcome mail to registered Student Email
                subject = 'Pheonix International school - Successfully Registered'
                message = f'Hi {student_name[0]},\n\nWelcome to Pheonix International School Student Portal. Your account has been activated, enroll classess right away!\n\nKind Regards,\nPrincipal\nPheonix International School\nBengaluru'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = email

                send_mail(
                    subject,
                    message,
                    email_from,
                    [recipient_list],
                    fail_silently=False
                )

                messages.success(
                    request, 'Successfully registered! Please login'
                )
                return redirect('login')
        else:
            # Alert Message: Password mismatch
            messages.error(
                request, 'Passwords do not match. Please try again.')
            return redirect('register')

    return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # Get form values from register.html
        username = request.POST['username']
        password = request.POST['password']

        # authenticate crediantls with database
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('login')

    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Successfully logged out')
        return redirect('index')


def dashboard(request):
    # Display enrolled classes on Dashboard
    enrolled_classes = Enrolled.objects.order_by(
        '-contact_date').filter(student_email__exact=request.user.email)

    context = {
        'enrolled_classes': enrolled_classes
    }
    print(context)

    return render(request, 'accounts/dashboard.html', context)
