from django.db import models
from django.db.models.fields import CharField, TextField, DateField
from django.db.models.fields.files import ImageField
import datetime


class Post(models.Model):
    title = CharField(max_length=120)
    description = TextField(default='')
    image = ImageField(upload_to="blog/images/")
    date = DateField(datetime.date.today)
