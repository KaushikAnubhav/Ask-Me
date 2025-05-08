from django import forms
from django.forms import ModelForm
from .models import Answer,Question,CustomUser
from better_profanity import profanity

profanity.load_censor_words()

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('detail',) 

    def clean_detail(self):
        detail = self.cleaned_data.get('detail')
        if profanity.contains_profanity(detail):
            raise forms.ValidationError("Your answer contains a restricted word.")
        return detail

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'detail', 'tags')

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if profanity.contains_profanity(title):
            raise forms.ValidationError("Your question title contains a restricted word.")
        return title

    def clean_detail(self):
        detail = self.cleaned_data.get('detail')
        if profanity.contains_profanity(detail):
            raise forms.ValidationError("Your question content contains a restricted word.")
        return detail

class ProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'bio', 'location')