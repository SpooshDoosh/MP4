from django import forms


class CommentForm(forms.Form):
    your_name = forms.CharField(max_length=30)
    comment_body = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return f'{self.comment_body} by {self.your_name}'


class SearchForm(forms.Form):
    title = forms.CharField(max_length=30)
