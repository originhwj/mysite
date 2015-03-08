from django.db import models
from django.contrib import admin
from django import forms
from django.forms import ModelForm

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    body2 = models.TextField()

    timestamp = models.DateTimeField()
    class Meta:
        ordering = ('-timestamp',)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp','body')

#class Item(models.Model):
#    name = models.CharField(max_length=250)
#    description = models.TextField()
#
#    class Meta:
#        ordering = ['name']
#
#    @models.permalink
#    def get_absolute_url(self):
#        return ('item_detail',None,{'object_id':self.id})

class Photo(models.Model):
    #item = models.ForeignKey(Item)
    title = models.CharField(max_length=100)
    image = models.ImageField("picture",upload_to='photos')
    caption = models.CharField(max_length=250,blank=True)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('photo_detail',None,{'object_id':self.id})

#class PhotoForm(ModelForm):
#    class Meta:
#        ModelForm.model = Photo
        #fields = '__all__'

#class PhotoInline(admin.StackedInline):
#    model = Photo
#
#class ItemAdmin(admin.ModelAdmin):
#    inlines = [PhotoInline]
#
#admin.site.register(Item,ItemAdmin)
admin.site.register(Photo)

admin.site.register(BlogPost,BlogPostAdmin)