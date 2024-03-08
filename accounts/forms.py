from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label_suffix='',label='',
        widget= forms.EmailInput(
            attrs= {
                'class':'form-control',
                'placeholder':'이메일'
            }
        )
    )
    username = forms.CharField(
        label_suffix='',label='',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'닉네임'
            }
        )
    )
    birthday = forms.DateField(
        label_suffix='',label='',
        widget=forms.DateInput(
            attrs={
                'type':'date',
                'class':'form-control',
            }
        )
    )
    password1 = forms.CharField(
        label_suffix='',label='',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'비밀번호',
            }
        )
    )
    password2 = forms.CharField(
        label_suffix='', label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호 재확인',
            }
        )
    )
    class Meta:
        model = get_user_model()
        fields = ('email','username','birthday','password1','password2',)

class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(
        label_suffix='',label='',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'닉네임'
            }
        )
    )
    class Meta:
        model= get_user_model()
        fields = ('username',)

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label_suffix='',label='',
        widget = forms.PasswordInput(
            attrs = {
                'class':'form-control',
                'placeholder':'기존 비밀번호',
            }
        )
    )
    new_password1 = forms.CharField(
        label_suffix='',label='',
        widget = forms.PasswordInput(
            attrs = {
                'class':'form-control',
                'placeholder':'새 비밀번호',
            }
        )
    )
    new_password2 = forms.CharField(
        label_suffix='',label='',
        widget = forms.PasswordInput(
            attrs = {
                'class':'form-control',
                'placeholder':'새 비밀번호 재입력',
            }
        )
    )
    class Meta:
        model = get_user_model()
        fields = ('old_password','new_password1','new_password2')

class CustomAuthenticationForm(AuthenticationForm):
    password = forms.CharField(
        label_suffix='',label='',
        widget= forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'비밀번호',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '이메일',
        })
    class Meta:
        model= get_user_model()
        fields= ('email','password',)