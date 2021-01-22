from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import validate_image_file_extension

# Create your models here.


class Portfolio(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    profile = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f"Portfolio ({self.name})"


class Image(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to="images", validators=[validate_image_file_extension])
    created_date = models.DateTimeField(default=datetime.now())
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f"Image ({self.name})"


class Comment(models.Model):
    comment = models.TextField()
    commented_date = models.DateTimeField(default=datetime.now())
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    profile = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f"Comment by ({self.profile})"
