from django.db import models
from django.urls import reverse

# Create your models here.
def get_absolute_url1(self):
			return f"/products/{self}/"