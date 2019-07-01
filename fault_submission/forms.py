from django import forms

from .models import fault

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)

class fault_form(forms.ModelForm):
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