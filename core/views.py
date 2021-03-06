from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact


# Create your views here.
def trigger_error(request):
    division_by_zero = 1 / 1


def home(request):
    return render(request, 'index.html')


def portfolio_details(request):
    return render(request, 'portfolio-details.html')


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            try:
                send_mail(subject, message, email, [
                    'jimmywilliamotieno@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
    return render(request, "index.html", {'form': form})
