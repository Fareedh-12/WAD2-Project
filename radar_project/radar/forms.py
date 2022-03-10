from django.contrib.auth.models import User
from radar.models import UserProfile
from django import forms

# Please update basing on the requirements of our implementation


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=128,
                               help_text="Please enter the username.")
    # if None or empty string is passed in, then clean() will raise
    # a ValidationError exception.
    username.clean("This field is required.")

    email = forms.EmailField()
    email.clean("invalid email address")
    
    password = forms.CharField(widget=forms.PasswordInput())
    password.clean("This field is required.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):

    picture = forms.ImageField
    class Meta:
        model = UserProfile
        fields = ('picture', 'host',)
