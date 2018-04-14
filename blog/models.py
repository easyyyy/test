from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    """
    Category - 种类
    Django 要求模型必须继承models.Model
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    Tag - 标签
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):

    #文章标题
    title = models.CharField(max_length=70)

    body = models.TextField()

    #创建时间 最后一次修改时间 modified - 修饰，改良
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    #摘要
    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']
    """
    
from django.utils import timezone
from django.contrib.auth.models import User
user = User.objects.get(username='lin')
c = Category.objects.get(name='category test')
p = Post(title='title test', body='body test', created_time=timezone.now(),category=c, modified_time=timezone.now(), author=user)
p.save()
Category.objects.all()
    """