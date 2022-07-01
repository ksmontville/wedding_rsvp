from django.shortcuts import render, redirect, get_object_or_404
from .forms import GuestForm, PasswordForm
from lockdown.decorators import lockdown


@lockdown()
def index(request):
    if request.method != 'POST':
        form = GuestForm
    else:
        form = GuestForm(data=request.POST)
        if form.is_valid():
            new_guest = form.save(commit=True)
            return redirect('rsvp:thank_you')

    context = {'form': form}
    return render(request, 'rsvp/index.html', context)


@lockdown()
def menu(request):
    return render(request, 'rsvp/menu.html')


@lockdown()
def events(request):
    return render(request, 'rsvp/events.html')


@lockdown()
def travel(request):
    return render(request, 'rsvp/travel_accommodations.html')


@lockdown()
def registry(request):
    return render(request, 'rsvp/registry.html')


@lockdown()
def about_us(request):
    return render(request, 'rsvp/about_us.html')


@lockdown()
def faqs(request):
    return render(request, 'rsvp/faqs.html')


@lockdown()
def thank_you(request):
    return render(request, 'rsvp/thank_you.html')


def password(request):
    if request.method != 'POST':
        password_form = PasswordForm
    else:
        password_form = PasswordForm(data=request.POST)
        if password_form.is_valid():
            return redirect('rsvp:index')

    context = {'password_form': password_form}

    return render(request, 'rsvp/password.html', context)
