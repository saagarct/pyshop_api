from django import forms
from .models import Status

class StatusForm(forms.ModelForm):
    class Meta:
        model= Status
        fields=[
            'user',
            'content'
        ]

    def clean_content(self,*args,**kwargs):
        content= self.cleaned_data.get('content')
        if len(content) > 250:
            raise forms.ValidationError("The content limitation is 250 words")
        return content


    def clean(self,*args, **kwargs):
        data= self.cleaned_data
        content= data.get('content', None)
        if content=="" or content==None:
            raise forms.ValidationError("No content provided")
        return super().clean(*args, **kwargs)
