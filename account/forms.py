from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required

User = get_user_model()


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'form-control',
                                          'placeholder': 'Password'
                                          }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'form-control',
                                          'placeholder': 'Confirm Password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
            'gender',
            'bio',
            'image',
        )

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }),

            'gender': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Gender'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Biography'
            })
        }

    # def clean(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')
    #     if password1 != password2:
    #         raise forms.ValidationError('password and confirm password is not same')
    #     return super().clean()



class LoginForm(forms.Form):
    email = forms.EmailField(max_length=40, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))
    #
    # class Meta:
    #     model = User
    #     fields = (
    #         'email',
    #         'password'
    #     )



class ChangePasswordForm(forms.Form):
  
    oldpassword = forms.CharField(
        widget=forms.PasswordInput(attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Old Password'
}))
    newpassword1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
                                          'class': 'form-control',
                                          'placeholder': 'New password'
                                          }),
        
    )
    newpassword2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Confirm Password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    def clean(self):
        newpassword1 = self.cleaned_data.get('newpassword1')
        newpassword2 = self.cleaned_data.get('newpassword2')
        if newpassword1 != newpassword2:
            raise forms.ValidationError('password and confirm password is not same')
        return super().clean()



