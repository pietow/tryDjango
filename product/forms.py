from django import forms


from .models import Product


class ProductForm(forms.ModelForm):
    title       = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "placeholder": "your title"
    }))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "new-class-name two",
        "placeholder": "your title",
        "id"   : "text-id",
        "rows" : 10,
        "cols" : 10
    }))
    price       = forms.DecimalField(initial=99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

#overriding title
   # def clean_title(self, *args, **kwargs):
   #     title = self.cleaned_data.get('title')
   #     if not 'CFE' in title:
   #         raise forms.ValidationError("This is not a valid title")
   #     if not 'news' in title:
   #         raise forms.ValidationError("This is not a valid title")
   #     return title

class rawProductForm(forms.Form):
    title       = forms.CharField(required=False)
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "new-class-name two",
        "placeholder": "your title",
        "id"   : "text-id",
        "rows" : 10,
        "cols" : 10
    }))
    price       = forms.DecimalField(required=False)
