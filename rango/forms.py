from django import forms
from rango.models import Page, Category, Contact
from django.contrib.auth.models import User
from rango.models import UserProfile


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.NAME_MAX_LENGTH, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=Page.TITLE_MAX_LENGTH, help_text="Please enter the name of the movie.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the movie.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    
    class Meta:
        model = Page
        exclude = ('category',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        return cleaned_data


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=Contact.NAME_MAX_LENGTH, help_text="Please enter name.")
    content = forms.CharField(max_length=Contact.NAME_MAX_LENGTH, help_text="Please enter the message.")
    email = forms.EmailField(widget=forms.EmailInput(), help_text="Please enter the address of your email.")

    class Meta:
        model = Contact
        fields = ('name', 'email', 'content')