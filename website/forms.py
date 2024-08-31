from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    
    # Disables the: 
    # https://stackoverflow.com/questions/78850636/what-is-password-based-authentication-in-the-usercreationform-in-django-and-how
    usable_password = None

    email = forms.EmailField(required=True, label="")
    first_name = forms.CharField(max_length=30, required=True, help_text="")
    last_name = forms.CharField(max_length=30, required=True, help_text="")
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control' , 'placeholder': 'Password Again'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        #     'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        # }

        # 'class': 'form-control' was removed since __init__ handles it, though I don't know which is more efficient 
        widgets = {
            # 'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            # 'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            # 'password2': forms.PasswordInput(attrs={'placeholder': 'Password Again'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }
        """
        Use the Meta class for static and straightforward form customizations like specifying model fields and setting basic widget attributes.
        Use the __init__ method for dynamic customizations or when you need to apply complex logic to form fields.
        """

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        """
        Django’s built-in UserCreationForm automatically provides reasonable defaults for help text and validation rules, 
        so you typically don’t need to manually set them unless you have specific requirements.
        e.g. bootstrap design
        """
        # help_texts = {
        #     'username': 'Enter a unique username.',
        #     'password1': 'Your password must be at least 8 characters long and include a mix of letters and numbers.',
        #     'password2': 'Enter the same password as above for verification.',
        # }
        
        # self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        # self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        # self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	



    def save(self, commit=True):

        """
        commit=True: Saves the instance to the database immediately.
        commit=False: Creates the instance but does not save it to the database.
        You can make additional modifications before saving it.
        """
        # Create a new user instance but do not save it yet
        user = super().save(commit=False)
        # Access validated data from cleaned_data
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if(commit):
            user.save()
        return user

