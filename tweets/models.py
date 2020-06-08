from django.db import models

# Create your models here.
# 3labali

class Tweet(models.Model):
    # id = models.AutoField(Primary_key=True)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to="images/", blank=True)

    def __str__(self):
        return self.content
    
