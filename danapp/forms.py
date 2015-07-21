from django import forms

class PreferenceForm(forms.Form):
  
    colorChoices = (
        ('Blue', 'Blue'),
        ('Red', 'Red'),
        ('Yellow', 'Yellow'),
    )
    colour = forms.ChoiceField(choices=colorChoices)
    font = forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder': 'Font'}))
    picture = forms.ImageField(required=False)