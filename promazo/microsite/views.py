import json

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, View, RedirectView

from django.contrib import messages

class HomePageView(RedirectView):
    """
    View for /
    Simply redirect to the sign-in page
    """
    url = '/sign-in'

def ProMazoHome(request):
    return render(request, 'microsite/index.html')

def ProMazoHow(request):
    return render(request, 'microsite/how-it-works.html')

def ProMazoHowStudent(request):
    return render(request, 'microsite/how-it-works-student.html')

def StudentStories(request):
    return render(request, 'microsite/student-stories.html')

def Student1(request):
    return render(request, 'microsite/stories/student-1.html')

def Student2(request):
    return render(request, 'microsite/stories/student-2.html')

def Student3(request):
    return render(request, 'microsite/stories/student-3.html')

def ProMazoHowCompany(request):
    return render(request, 'microsite/how-it-works-company.html')

def CorporateWork(request):
    return render(request, 'microsite/corporate-work.html')

def Corporate1(request):
    return render(request, 'microsite/work/corporate-1.html')

def Corporate2(request):
    return render(request, 'microsite/work/corporate-2.html')

def Corporate3(request):
    return render(request, 'microsite/work/corporate-3.html')

def Corporate4(request):
    return render(request, 'microsite/work/corporate-4.html')

def About(request):
    return render(request, 'microsite/about.html')

def ContactPM(request):
    return render(request, 'microsite/contact-pm.html')

def ContactUs(request):
    return render(request, 'microsite/contact-us.html')

def ContactSend(request):
    # get the name
    name = 'No Name Entered'
    if 'name' in request.GET and request.GET['name'] != '':
        name = request.GET['name']

    # get the email
    email = 'No Email Entered'
    if 'email' in request.GET and request.GET['email'] != '':
        email = request.GET['email']

    # get the message
    message = 'No Message Entered'
    if 'message' in request.GET and request.GET['message'] != '':
        message = request.GET['message']
    import smtplib

    # Import MIMEText and MIMEMultipart for fancy email header modifications (to, from, subject, etc)
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    # The actual text of the message (body)
    message_text = "NAME: " + name + "\nEMAIL: " + email + "\n\n" + message

    # The subject of the email
    subject = "Message from ProMazo.com"

    # Who sends this message (must include domain name, no spaces)
    sender = "ContactUs@promazo.com"

    # Who will receive this email?
    recipient = "brett@promazo.com"

    # Create a new message object - this object will have multiple "parts" to it,
    # including a message, subject, to/from, etc.  This message object DOES have the ability
    # to attach other objects, such as local files as "attachments"
    message = MIMEMultipart('alternative')

    # Create a new text object, which will hold our main message.  Note that there are various types of
    # these objects that we can add: 'plain' or 'html'.  Since some servers block HTML-formatted messages (or turn off formatting),
    # it's usually a good idea to always generate a 'plain' text message.
    message_body = MIMEText(message_text, 'plain')

    # Now we generate the content of our message object, by setting up the To, From, and Subject headers
    message['To'] = recipient
    message['From'] = sender
    message['Subject'] = subject

    # Add our message body as an attachment
    message.attach(message_body)

    email = smtplib.SMTP('localhost')

    email.sendmail(sender, recipient, message.as_string())

    email.quit()
    return HttpResponse('200')
