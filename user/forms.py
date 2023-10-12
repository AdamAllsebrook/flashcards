from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Username")
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password")
    password_confirm = forms.CharField(label="Confirm Password")

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return password_confirm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="Username")
    password = forms.CharField(label="Password")
