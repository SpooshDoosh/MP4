from django import forms
from .models import CommentMod


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentMod
        fields = ('your_name', 'comment_body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'your_name': 'Name',
            'comment_body': 'Comment',
        }

        self.fields['your_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'comment-form-input'
            self.fields[field].label = False

    def __str__(self):
        return f'{self.comment_body} by {self.your_name}'


class SearchForm(forms.Form):
    title = forms.CharField(max_length=30)
