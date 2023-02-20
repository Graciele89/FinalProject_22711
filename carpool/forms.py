from django import forms


class PostForm(forms.Form):
    # image = forms.FileField()
    text = forms.CharField(label="Your destination:")
    text = forms.CharField(label="Your origin:")
    text = forms.DateTimeField(label="Day & Time")
