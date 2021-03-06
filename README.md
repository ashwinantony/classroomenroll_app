# classroomenroll_app

Dear fellow Django developer,

In order for the Welcome E-Mail system work - Please follow the steps below.

Enter the Host/Sender Email ID and Password in the settings.py of 'project_enroll' folder.

    Open 'project_enroll' -> settings.py -> Update Lines 143 and 144.
    ==> FROM THIS
        EMAIL_HOST_USER = ''
        EMAIL_HOST_PASSWORD = ''

    ==> TO sender’s mail id and password
        EMAIL_HOST_USER = 'Eg-xxx@gmail.com'
        EMAIL_HOST_PASSWORD = 'Eg-gmail_password'

After these extra lines of code has been added to your project, you can send emails now. But if you are using Gmail, then the first time you make these changes in your project and run, you might get SMTP error.

To correct that-
1. Go to the Google account registered with the sender’s mail address and select Manage your account
2. Go to security section at the left nav and scroll down. In Less secure app access, turn on the access. By default, it would be turned off.
3. Finally run the application.

Now, register any user to your application, and they will receive mail from the email account you had mentioned.
Cheers!

Regards,
Ashwin
