from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile


class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["occupation", "age", "location"]
