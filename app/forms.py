from django import forms

class Student(forms.Form):
    name=forms.CharField(max_length=50)
    age=forms.IntegerField()