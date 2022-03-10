from django.contrib.auth.models import User
from radar.models import UserProfile
from django import forms

# Please update basing on the requirements of our implementation


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=128,
                               help_text="Please enter username.")
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=128,
                               help_text="Please enter your first name.")
    last_name = forms.CharField(max_length=128,
                               help_text="Please enter your last name.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class UserProfileForm(forms.ModelForm):
    age = forms.IntegerField()
    picture = forms.ImageField()
    class Meta:
        model = UserProfile
        fields = ('age','picture')
