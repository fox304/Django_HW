from django import forms

from myhomeapp.models import Product


class ImageForm(forms.Form):
    photo = forms.ImageField(label='фото продукта')
    product = forms.ModelChoiceField(queryset=Product.objects.all(),label="для какого продукта")
