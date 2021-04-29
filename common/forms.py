from django import forms

from common.models import Subscriber,Comment


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = (
            'email',
        )
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'full_name',
            'email',
            'comment',
            'parent_comment'
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
            'parent_comment': forms.HiddenInput()
        }