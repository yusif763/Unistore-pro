from django import forms

from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'full_name',
            'email',
            'message'
        )
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email'
            }),

            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
                'cols': 50,
            })
        }
