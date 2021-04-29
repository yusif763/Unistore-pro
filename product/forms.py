from django import forms

from product.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'full_name',
            'email',
            'comment',
            'parent_comment',
        )
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'comment': forms.TextInput(attrs={
                'class': 'form-control',
                'cols': 50,
                'placeholder': 'Type Here'
            }),
            'parent_comment': forms.HiddenInput(),
        }