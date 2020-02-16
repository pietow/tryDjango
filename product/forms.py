from django import forms


from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class rawProductForm(forms.Form):
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
    price       = forms.DecimalField(required=False)
