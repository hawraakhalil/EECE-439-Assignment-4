# mysite1/myapp1/forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "address", "profession", "tel_number", "email"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Full name"}),
            "address": forms.TextInput(attrs={"class": "form-control", "placeholder": "Address"}),
            "profession": forms.TextInput(attrs={"class": "form-control", "placeholder": "Profession"}),
            "tel_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "+9617xxxxxx"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "name@example.com"}),
        }

class ContactSearchForm(forms.Form):
    q = forms.CharField(
        label="Search",
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Name, email, profession…"})
    )
