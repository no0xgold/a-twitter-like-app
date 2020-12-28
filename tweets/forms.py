from django import forms
from django.core.exceptions import ValidationError


from django.conf import settings



from .models import Tweet

MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH 
class TweetForms(forms.ModelForm):
 
    class Meta:
        model = Tweet
        fields = ['content']
    
    
    
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("This is too long")
        return content