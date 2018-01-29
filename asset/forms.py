from django import forms
from django.urls import reverse_lazy
from dal import autocomplete
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, ButtonHolder, Submit, Reset, Button, HTML
from crispy_forms.bootstrap import AppendedText

from .models import Asset, Organization

class AssetCreateForm(forms.ModelForm):
    """
    Form for the creation or update a new data asset
    """
    parent = forms.ModelChoiceField(queryset=Asset.objects.filter(parent=None),
                                    required=False,
                                    empty_label='Select the parent asset, if applicable.')

    def __init__(self, *args, **kwargs):
        super(AssetCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div('name', css_class= 'form-group col-md-10'),
                Div('parent', css_class= 'form-group col-md-10'),
                Div('subject_tags', css_class= 'form-group col-md-10'),
                Div('status', css_class= 'form-group col-md-4'),
                Div('description', css_class= 'form-group col-md-10'),
                Div('isContracted', css_class= 'form-group col-md-12'),
                Div('spatial_scale', css_class= 'form-group col-md-4'),
                css_class= 'form-row'
            ),
            Div(
                Div('start_month', css_class= 'form-group col-md-2'),
                Div('end_month', css_class= 'form-group col-md-2 offset-md-1'),
                css_class = 'form-row'
            ),
            Div(
                Div('start_year', css_class= 'form-group col-md-2'),
                Div('end_year', css_class= 'form-group col-md-2 offset-md-1'),
                Div('place_tags', css_class= 'form-group col-md-10'),
                css_class= 'form-row',
            ),
            Div(
                Div('organization', css_class='form-group col-md-7'),
                Div('primary_contact_name', css_class='form-group col-md-7'),
                css_class = 'form-row',
            ),
            Div(
                Div('primary_contact_email', css_class= 'form-group col-md-4'),
                Div('primary_contact_phone', css_class= 'form-group col-md-3'),
                Div('primary_contact_phone_ext', css_class= 'form-group col-md-1'),
                Div('primary_contact_address1', css_class= 'form-group col-md-8'),
                Div('primary_contact_address2', css_class= 'form-group col-md-8'),
                css_class= 'form-row'
            ),
            Div(
                Div('primary_contact_city', css_class= 'form-group col-md-5'),
                Div('primary_contact_state', css_class= 'form-group col-md-2'),
                Div('primary_contact_zip', css_class = 'form-group col-md-1'),
                css_class = 'form-row'
            ),
            HTML("<div class='my-5'></div>"),
            Div(
                HTML('<input id="copy_contact_info" name="copy_contact" type="checkbox" onchange="copyContactHandler(this)">'),
                HTML('<label for="copy_contact_info">Contact for data is the same as primary contact</label>'),
                css_class = 'form-row',
                ),
            Div(
                Div('data_contact_name', css_class='form-grouo col-md-7'),
                css_class= 'form-row'
            ),
            Div(
                Div('data_contact_email', css_class= 'form-group col-md-4'),
                Div('data_contact_phone', css_class= 'form-group col-md-3'),
                Div('data_contact_phone_ext', css_class= 'form-group col-md-1'),
                css_class= 'form-row'
            ),
            Div(
                Div('data_contact_address1', css_class= 'form-group col-md-8'),
                Div('data_contact_address2', css_class= 'form-group col-md-8'),
                css_class= 'form-row'
            ),
            Div(
                Div('data_contact_city', css_class= 'form-group col-md-5'),
                Div('data_contact_state', css_class= 'form-group col-md-2'),
                Div('data_contact_zip', css_class = 'form-group col-md-1'),
                css_class= 'form-row'
            ),
            Div(
                Div('partners', css_class= 'form-group col-md-10'),
                css_class= 'form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Save', css_class='btn btn-primary')
                )
            )

    class Meta:
        model = Asset
        fields = '__all__'
        widgets = {
            'subject_tags':
                autocomplete.TaggitSelect2(url='asset:get-subject-tags',
                    attrs={'class':'form-control'},
                ),
            'place_tags':
                autocomplete.TaggitSelect2(url='asset:get-place-tags',
                    attrs={'class':'form-control'},
                ),
            'primary_contact_address2':
                forms.TextInput(attrs={'placeholder': 'Building, Suite, Floor, Mailstop'},
                ),
            'data_contact_address2':
                forms.TextInput(attrs={'placeholder': 'Building, Suite, Floor, Mailstop'},
                ),
            'primary_contact_email':
                forms.TextInput(attrs={'placeholder': 'john_simth@fws.gov'},
                ),
            'primary_contact_phone':
                forms.TextInput(attrs={'placeholder': '(123) 222-4545'},
                ),
            'data_contact_phone':
                forms.TextInput(attrs={'placeholder': '(123) 222-4545'},
                ),
        }


class AssetListFormHelper(FormHelper):
    """
    """
    model = Asset
    form_tag = False
    form_show_labels = False

    layout = Layout(
        'name',
        'status',
        'organization__region',
        ButtonHolder(
            Submit('submit', 'Filter', css_class='button btn-primary'),
        )
    )


class AssetFilterForm(forms.Form):
    """ """
    def __init__(self, *args, **kwargs):
        super(AssetFilterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.disable_csrf = True
        self.helper.form_method = 'GET'
        self.helper.form_show_labels = False
        self.helper = Layout(
            Div(
                Div('organization__region', css_class='col'),
                Div('name', css_class='col'),
                Div('status', css_class='col'),
                css_class='form-row'),
            ButtonHolder(
                Submit('submit', 'Filter', css_class='button btn-primary btn-sm'),
            )
        )

    class Meta:
        fields = ('organization__region','name','status')
        widgets = {
            'organization__region': forms.TextInput(attrs={'placeholder': 'Region',
                                                            'class': 'form-control-small'}),
            'name': forms.TextInput(attrs={'placeholder': 'Asset Name contains',
                                            'class': 'form-control-small'}),

        }
