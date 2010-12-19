from django import forms
from models import Host

class HostForm(forms.ModelForm):
    class Meta:
        model = Host 
        exclude = ('slug','referral_url','large_image','small_image_one','small_image_two','featured','approved',)
