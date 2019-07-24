from django import forms

from .models import fault

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML, Div
from pyuploadcare.dj.forms import FileWidget, ImageField

# This form uses the crispy_form layout helper heavily. 
# More details on its usage can be found here: https://django-crispy-forms.readthedocs.io/en/d-0/layouts.html
TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)

class fault_form(forms.ModelForm):
    photo = ImageField(widget=FileWidget(attrs={
        'data-public-key':'1164fee45dc9e007b701',
        'data-images-only':'True',
        'data-preview-step':'True',
    }))
    
    contacted_on_updates = forms.ChoiceField(
        label="Do you wish to be contacted on the updates?",
        choices=TRUE_FALSE_CHOICES, 
        widget=forms.RadioSelect()
    )
    agree_to_clauses = forms.BooleanField(
        label="I have read and agree to the Terms and Conditions and Privacy Policy"
    )
    
    class Meta:
        model = fault
        fields = '__all__'
        exclude = ('followed_up','date_of_creation',)
    
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
                                Fault Reporting Form
                            </h3>
                            """
                        )
                    )
                )
            ),
            Row(
                Column(
                    Div(
                        HTML(
                            """
                            <p>
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
                                Sed aliquet nisi risus, eu blandit turpis pharetra faucibus. 
                                Mauris dolor orci, malesuada sed ipsum vitae, 
                                tincidunt molestie justo. 
                                Donec rhoncus iaculis mi, 
                                ac laoreet est sollicitudin sit amet. 
                                Sed suscipit eleifend neque sit amet iaculis. 
                                Donec ut urna ac erat convallis condimentum. 
                                Suspendisse placerat lorem tortor, sed tempus nunc blandit ac. 
                                Donec iaculis turpis non libero eleifend,
                                quis volutpat turpis sagittis. 
                                Ut vel nibh congue diam ullamcorper dapibus. 
                                Donec finibus sapien ut tristique semper. 
                                Nulla accumsan elementum tincidunt.
                            </p>
                            """
                        )
                    )
                )
            ),
            Row(
                Column(
                    Div(
                        HTML(
                            """
                            <h5>
                                Contact Details
                            </h5>
                            """
                        ),
                        css_class='green-text'
                    )
                )
            ),
            Row(
                Column(
                    'name', 
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
                    'phone_number', 
                    css_class='form-group col-12'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    'contacted_on_updates',
                    css_class='form-group col-12'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    Div(
                        HTML(
                            """
                            <h5>
                                Report Details
                            </h5>
                            """
                        ),
                        css_class='green-text'
                    )
                )
            ),
            Row(
                Column(
                    'description', 
                    css_class='form-group col-12'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    'photo', 
                    css_class='form-group col-12'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    'agree_to_clauses', 
                    css_class='form-group col-12'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    Submit(
                        'submit', 
                        'Post Fault', 
                        css_class="btn btn-primary w-50"
                    ),
                    css_class='form-group col-12 text-center'
                ),
                css_class='form-row'
            ),
        )