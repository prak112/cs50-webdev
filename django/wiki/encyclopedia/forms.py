from django import forms


# form fields for new_entry & edit_entry
class NewForm(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={'placeholder':'Title here...'}))
    content = forms.CharField(widget=forms.Textarea(attrs=
                                                    {'rows': 10, 'cols': 40, 'placeholder':'Enter Content in Markdown syntax...'}))
    submit = forms.CharField(widget=forms.widgets.Input(attrs={'type':'submit', 'value':'Submit!'}))
  
# form fields for search view
class SearchForm(forms.Form):
    search_term = forms.CharField(label="Search", required=True, widget=forms.TextInput(attrs={'placeholder':'Search Encyclopedia...'}))
    submit = forms.CharField(widget=forms.widgets.Input(attrs={'type':'submit', 'value':'Search!'}))