from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings


class News(models.Model):
    CATEGORY =(("0","Politics"),("1","Sports"),("2","International"))
    title = models.CharField(max_length=250)
    story = models.TextField(verbose_name='Article')
    category = models.CharField(choices=CATEGORY, max_length=2)
    slug = models.CharField(max_length=270)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="newes")
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    cover_image = models.ImageField(upload_to='uploads')

    class Meta:
        verbose_name_plural = "News"
        db_table = "news_db" 


    def get_absolute_url(self):
        return reverse("detail_news", kwargs={"category": self.get_category_display().lower(), "pk":self.pk})

    
    def __str__(self):
        return self.title



class Comment(models.Model):
    news                =   models.ForeignKey(News, on_delete=models.CASCADE, related_name="article")
    feedback            =   models.TextField()
    commentor           =   models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{ self.news } : { self.feedback }"
