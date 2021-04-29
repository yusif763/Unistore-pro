from django import forms

from checkout.models import CheckOut


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = CheckOut
        fields = (
            'reciever',
            'phone',
            'email',
            'city',
            'street',
            'building',
            'zip_code',
            'payment',
            'promo_code',
            'country'
        )
        widgets = {
            'reciever': forms.TextInput(attrs={
                'class':'form-control',
                'value': 'Yusif Huseynli'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'cols': 50,
                'value': '+994 144546464'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'value': 'sadasda@gmail.com'
            }),
            'country': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Country'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'street': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'building': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'zip_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'payment': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Payment'
            }),
            'payment': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Payment'
            }),
            'promo_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Promo code'
            }),
        }