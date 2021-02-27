from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(verbose_name='Title', max_length=255)
    pub_date = models.DateTimeField(verbose_name='Publication Date', auto_now=True)
    body = models.TextField(verbose_name='Body')
    image = models.ImageField(verbose_name='Product Image', upload_to='images/')
    url = models.URLField(verbose_name='URL')
    votes_total = models.IntegerField(default=1)
    icon = models.ImageField(verbose_name='Product Icon', upload_to='images/')
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
