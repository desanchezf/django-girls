
from django.conf import settings
from django.db import models
from django.forms import DateTimeField
from django.utils import timezone

# Create your models here.

class Post(models.Model): 

    # Attributes
    author: models.ForeignKey = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    title: models.CharField = models.CharField(max_length=200)
    text: models.TextField = models.TextField()
    created_date = models.DateTimeField(
        default = timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, 
        null=True
    )

    # Methods
    def publish(self) -> None: 

        self.published_date = timezone.now()
        self.save()
    
    def __str__(self) -> str:

        object = "author" + str(self.author) + "\n"
        object += "title" + str(self.title) + "\n"
        object += "text" + str(self.text) + "\n"
        object += "created_date" + str(self.created_date) + "\n"
        object += "created_date" + str(self.published_date) + "\n"
        
        return object