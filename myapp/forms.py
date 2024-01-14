from .models import Blog
from django import forms
from django.contrib.auth.models import User
class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields=['username', 'password']
        widgets ={
            'password':forms.PasswordInput(),

        }
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']