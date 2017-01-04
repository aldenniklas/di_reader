# coding=utf-8

from django import forms

class UnlockForm(forms.Form):
    article = forms.URLField(required=True, label='Kopiera in din länk här')