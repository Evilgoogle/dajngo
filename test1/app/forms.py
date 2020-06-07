from django import forms

class MyAdminForm(forms.ModelForm):
    pass

class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)