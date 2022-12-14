from django.contrib.auth.forms import forms
from home.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'user_name',
            'email',
            'phn_number',
            'comment'

        ]
