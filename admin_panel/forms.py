from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML, Div

class SignInForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(
        required=True, 
        widget=forms.PasswordInput
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(
                    Div(
                        HTML(
                            """
                            <h3>
                                Sign In
                            </h3>
                            """
                        )
                    )
                )
            ),
            Row(
                Column(
                    'username', 
                    css_class='form-group col-12'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    'password', 
                    css_class='form-group col-12'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    Submit(
                        'submit', 
                        'Sign In', 
                        css_class="btn btn-primary w-50"
                    ),
                    css_class='form-group col-12 text-center'
                ),
                css_class='form-row'
            ),
        )


class RegisterUserForm(UserCreationForm):
    
    password1 = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput
    )
    
    class Meta:
        model = User
        fields = (
            'username', 
            'email', 
            'password1', 
            'password2'
        )
        
    def clean_username(self):
        requested_username = self.cleaned_data.get('username')
        if User.objects.filter(username=requested_username).count() > 0:
            raise forms.ValidationError("This username is already taken.")
        return requested_username
    
    def clean_email(self):
        requested_email = self.cleaned_data.get('email')
        if User.objects.filter(email=requested_email).count() > 0:
            raise forms.ValidationError("This email is already in use")
            
        return requested_email
            
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
    
        if (password1 != password2):
            raise forms.ValidationError("The passwords must match!")
            
        return password2
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(
                    Div(
                        HTML(
                            """
                            <h3>
                                Sign Up
                            </h3>
                            """
                        )
                    )
                )
            ),
            Row(
                Column(
                    'username', 
                    css_class='form-group col-12'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    'email', 
                    css_class='form-group col-12'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    'password1', 
                    css_class='form-group col-12'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    'password2', 
                    css_class='form-group col-12'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    Submit(
                        'submit', 
                        'Sign Up', 
                        css_class="btn btn-primary w-50"
                    ),
                    css_class='form-group col-12 text-center'
                ),
                css_class='form-row'
            ),
        )