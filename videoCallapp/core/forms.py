from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100,required=True, help_text='Required. Enter a valid email address.')
    first_name = forms.CharField(max_length=50, required=True, help_text='Required. Enter your first name.')
    last_name = forms.CharField(max_length=50, required=True, help_text='Required. Enter your last name.')

    class Meta:
        model = User  # Replace 'User' with your custom user model if applicable
        fields = (  'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self,commit=True):
        user = super(RegisterForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user 
