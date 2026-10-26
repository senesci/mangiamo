from django import forms

from .models import Author

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

class RecipeForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    author = forms.ChoiceField(label='Author', widget=forms.Select, help_text="If you are a new author, type it in with your recipe.")
    body = forms.CharField(label='Recipe', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].choices = [
            (author.id, author.name) for author in Author.objects.all().order_by('name')
        ]