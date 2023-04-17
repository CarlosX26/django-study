from django import forms
from cars.models import Car

# class CarForm(forms.Form):
#     brand = forms.CharField(
#         max_length=32,
#         label="Marca",
#         widget=forms.TextInput(attrs={"placeholder": "Digite a marca do carro"}),
#     )
#     model = forms.CharField(
#         max_length=64,
#         label="Modelo",
#         widget=forms.TextInput(attrs={"placeholder": "Digite o modelo do carro"}),
#     )
#     color = forms.CharField(
#         max_length=32,
#         label="Cor",
#         widget=forms.TextInput(attrs={"placeholder": "Digite a cor do carro"}),
#     )
#     year = forms.IntegerField(
#         min_value=1,
#         label="Ano",
#         widget=forms.NumberInput(attrs={"placeholder": "Digite o ano do carro"}),
#     )


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        labels = {
            "brand": "Marca",
            "model": "Modelo",
            "color": "Cor",
            "year": "Ano",
        }
        widgets = {
            "brand": forms.TextInput(attrs={"placeholder": "Digite a marca do carro"}),
            "model": forms.TextInput(attrs={"placeholder": "Digite o modelo do carro"}),
            "color": forms.TextInput(attrs={"placeholder": "Digite a cor do carro"}),
            "year": forms.NumberInput(attrs={"placeholder": "Digite o ano do carro"}),
        }
