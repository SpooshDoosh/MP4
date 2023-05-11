from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __innit__(self, *args, **kwargs):
        placeholders = {
            'deafult_phone_number': 'Contact Number',
            'deafult_street_address1': '1st Line of Street Address',
            'deafult_street_address2': '2nd Line of Street Address',
            'deafult_town_or_city': 'Town or City',
            'deafult_county': 'County',
            'deafult_postcode': 'Postcode',
            'deafult_country': 'Country',
        }

        self.fields['deafult_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False
