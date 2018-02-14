from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
	name=models.CharField(max_length=200)
	slug = models.SlugField(null=True, blank=True, max_length=200)
	

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		return super(Category, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('main:category', kwargs={'slug': self.slug})



class Video(models.Model):
	link=models.URLField()
	title=models.CharField(max_length=200)
	img_url=models.URLField(null=True)
	video_id=models.CharField(max_length=200)
	created_date=models.DateTimeField(auto_now_add=True)
	category=models.ForeignKey(Category)
	feature=models.BooleanField(default=False)
	slug = models.SlugField(null=True, blank=True, max_length=200)
	
	
	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		
		self.img_url='https://img.youtube.com/vi/'+self.video_id+'/0.jpg'
		self.link='https://www.youtube.com/watch?v='+self.video_id
		return super(Video, self).save(*args, **kwargs)


	





