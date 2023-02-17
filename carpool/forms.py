from django import forms


class PostForm(forms.Form):
    # image = forms.FileField()
    text = forms.CharField(label="Your destination:")
    # text = forms.CharField(label="Pick up point:")
    # text = forms.CharField(label="Day")
    # text = forms.CharField(label="Time")
