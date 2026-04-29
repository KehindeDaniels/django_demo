from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(label = "Email", widget=forms.EmailInput(
        attrs={
            'placeholder':'example@gmail.com'
        }
    ))
    
    phone = forms.CharField(
        label='Phone',
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. +1234567',
            'type': 'tel'
        })
    )
    message = forms.CharField(widget=forms.Textarea)
