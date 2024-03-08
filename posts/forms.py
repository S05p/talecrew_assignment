from django import forms
from posts.models import *


class PostForm(forms.Form):
    title = forms.CharField(
        label_suffix='',label='',
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'제목',
            }
        )
    )
    content = forms.CharField(
        label_suffix='',label='',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'내용'
            }
        )
    )
    price = forms.IntegerField(
        label_suffix='',label='',
        widget=forms.TextInput(
            attrs={
                'type':'number',
                'class':'form-control',
                'placeholder':'가격',
            }
        )
    )
    class Meta:
        model = Post
        fields = ('title','content','price',)



