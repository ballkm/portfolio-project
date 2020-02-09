from django.db import models

#Create A blog models
#title
#pub_date
#body
#image

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    iamge = models.ImageField(upload_to='images/')


# Add the Blog app to the setting

#Create a migration

#Migrate

#Add to the admin