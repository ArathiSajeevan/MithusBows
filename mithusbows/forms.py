from django import forms

class regform(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    contact = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    cpassword = forms.CharField(max_length=20)

class logform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)

class itemform(forms.Form):
    image = forms.FileField()
    itemname = forms.CharField(max_length=20)
    description = forms.CharField(max_length=80)
    price = forms.IntegerField()

