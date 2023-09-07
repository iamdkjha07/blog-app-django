from django.db import models


# Create your models here.
class contactForm(models.Model):
    fname = models.CharField(max_length=100)
    emailId = models.EmailField()
    phoneNo = models.CharField(max_length=12)
    subject = models.CharField(max_length=100)
    messageContent = models.TextField()
    
    def __str__(self) -> str:
        return self.fname
    
class popularblog(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    contentBox = models.TextField()
    imageBox = models.ImageField(upload_to="webBlog/", max_length=250, null=True, default=None)
    
    def __str__(self) -> str:
        return self.title
    

class recentlyAdded(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    contentBox = models.TextField()
    imageBox = models.ImageField(upload_to="recentBlog/", max_length=250, null=True, default=None)
    
    def __str__(self) -> str:
        return self.title
    
class WebBlog(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    contentBox = models.TextField()
    imageBox = models.ImageField(upload_to="webBlog/", max_length=250, null=True, default=None)
    
    def __str__(self) -> str:
        return self.title
    
    
class AppBlog(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    contentBox = models.TextField()
    imageBox = models.ImageField(upload_to="appBlog/", max_length=250, null=True, default=None)
    
    def __str__(self) -> str:
        return self.title