from django import forms


class TodolistForm(forms.Form):
    text = forms.CharField(max_length=50,
           widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter todo e.g. Wash my car', 'aria-label': 'Todo', 'aria-describedby': 'add-btn' }))
