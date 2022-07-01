from django import forms

from .models import Guest


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'address', 'city', 'state', 'zip', 'email', 'phone']
        labels = {
            'name': 'Name',
            'address': 'Address',
            'city': 'City',
            'state': 'State*',
            'zip': 'Zip Code*',
            'email': 'Email',
            'phone': 'Phone*',
        }


class PasswordForm(forms.Form):
    password = forms.CharField(label='Password', max_length=10)
