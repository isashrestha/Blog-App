from django.db import models
from django.contrib.auth.models import User



STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique = True)
    author = models.CharField(max_length=200, unique = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default =0)

    def __str__(self):
        return self.title
        

 


