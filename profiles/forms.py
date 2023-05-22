from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        placeholders = {
            'default_phone_number': 'Contact Number',
            'default_street_address1': '1st Line of Street Address',
            'default_street_address2': '2nd Line of Street Address',
            'default_town_or_city': 'Town or City',
            'default_county': 'County',
            'default_postcode': 'Postcode',
            'default_country': 'Country',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False
