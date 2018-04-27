from django import forms
from django.forms import ModelForm
from shop.models import Good, Category


class NewCatForm(ModelForm):

    class Meta:
        model=Category
        fields=['name', 'slug','description', 'image']

class NewGoodForm(ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Good Name'})) 
    slug = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'must be same as description, use dash to replace the space'})) 
    
    detail = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Input Detail'})) 

    #category = forms.ChoiceField(choices=Category.objects.values_list('description', 'name'))

    #image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control', 'required': False})) 

    #category.widget.attrs.update({'class':'form-control'})
    class Meta:
        model = Good
        fields= ['description', 'slug', 'detail', 'category', 'image']
