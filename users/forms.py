from django import forms
from users.models import User

# class UserForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     password = forms.CharField()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        labels = {
            "username": "Nome de usúario",
            "email": "Email",
            "password": "Senha",
        }
        widgets = {
            "username": forms.TextInput(
                attrs={"placeholder": "Digite seu nome de usúario"}
            ),
            "email": forms.EmailInput(attrs={"placeholder": "Digite seu email"}),
            "password": forms.PasswordInput(attrs={"placeholder": "Digite sua senha"}),
        }

    def save(self, commit: bool = ...) -> any:
        return User.objects.create_user(**self.cleaned_data)
