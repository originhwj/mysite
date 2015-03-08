from django.forms import ModelForm
from blog.models import Photo

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields =('title','image')
