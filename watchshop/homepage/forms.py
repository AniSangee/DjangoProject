from .models import WatchUpload
from django import forms

class uploadform(forms.ModelForm):
    name = forms.CharField(
        widget = forms.TextInput(attrs={'class':'form-control'}),
        required=True
    )

    price = forms.DecimalField(
        widget = forms.NumberInput(attrs={'class':'form-control'}),
        required=True
    )

    description = forms.CharField(
        widget = forms.Textarea(attrs={'class':'form-control', 'rows': 3}),
        required=True
    )

    image = forms.CharField(
        widget = forms.ClearableFileInput(attrs={'class':'form-control'}),
        required=True
    )



    class Meta:
        model= WatchUpload
        fields= ['name','description','price','image']