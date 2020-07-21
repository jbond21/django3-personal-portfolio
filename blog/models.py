from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 200)
    date = models.DateField()
    image = models.ImageField(upload_to = 'portfolio/images/')
    image_title = models.CharField(max_length = 200)
    image_description = models.TextField(max_length = 200)
    image2 = models.ImageField(upload_to = 'portfolio/images/')
    image_title2 = models.CharField(max_length = 200)
    image_description2 = models.TextField(max_length = 200)
    image3 = models.ImageField(upload_to = 'portfolio/images/')
    image_title3 = models.CharField(max_length = 200)
    image_description3 = models.TextField(max_length = 200)
    image4 = models.ImageField(upload_to = 'portfolio/images/')
    image_title4 = models.CharField(max_length = 200)
    image_description4 = models.TextField(max_length = 200)
    image5 = models.ImageField(upload_to = 'portfolio/images/')
    image_title5 = models.CharField(max_length = 200)
    image_description5 = models.TextField(max_length = 200)
    image6 = models.ImageField(upload_to = 'portfolio/images/')
    image_title6 = models.CharField(max_length = 200)
    image_description6 = models.TextField(max_length = 200)

    def __str__(self):
        return self.title
