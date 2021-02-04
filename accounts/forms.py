from django import forms
from user.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(label="패스워드", widget=forms.PasswordInput)
    password2 = forms.CharField(label="패스워드 확인", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password", "password2")
        labels= {
            "username": "아이디",
            }
    

    def clean_password2(self):
        check = self.cleaned_data
        if check.get("password") != check.get("password2"):
            raise forms.ValidationError("패스워드가 일치하지 않아요")
        return check