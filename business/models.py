from django.db import models

# Create your models here.

class HeroSection(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    background_image = models.ImageField(upload_to='media/')

    def __str__(self):
        return f"{self.title}"

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    profile_pic = models.FileField(upload_to='team/',default="profile.png")
    twitter_url = models.CharField(max_length=55,blank=True,null=True)
    facebook_url = models.CharField(max_length=55,blank=True,null=True)
    instagram_url = models.CharField(max_length=55,blank=True,null=True)
    tiktok_url = models.CharField(max_length=55,blank=True,null=True)

    def __str__(self):
        return f"({self.name}--------{self.position})"
    
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50) 

    def __str__(self):
        return f"{self.name}"

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/')
    description = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.category})"

class ContactInfo(models.Model):
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.address}, {self.phone}, {self.email}"

class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=55)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name} - {self.email}"

class Testimonial(models.Model):
    profile_image = models.ImageField(upload_to='testimonial/')
    name=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    
    message=models.TextField()

    def __str__(self):
        return f"Testimonial by {self.name}"