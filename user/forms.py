from django import forms

class LoginForm(forms.form):
    '''authenticate users against the database'''

    username = forms.CharField(    )
    password = forms.CharField(widjet=forms.PassworInput)

