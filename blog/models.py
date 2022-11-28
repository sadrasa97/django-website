from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=255)
        
    def __str__(self):
        return self.name
    
class Post(models.Model):
    image=models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=250)
    content=models.TextField()
    #tags
    category=models.ManyToManyField(Category)
    counted_views=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    publish_date=models.DateTimeField(auto_now=True,null=True)
    
    class Meta:
        ordering=['created_at']
        verbose_name='پست '
        verbose_name_plural='پست ها '
    
    def __str__(self):
        return self.title
    
    def snippets(self):
        return self.content[:200] + '...'
    
    
    #SELESCT * FROM POST
    #SELECT * FROM POST WHERE STATUS =1
    
    ####################################
    #python manage.py shell
    #from blog.models import Post
    #p1=Post()
    #p1.title='test title'
    #p1.content='this is the firt test'
    #Post.objects.all()...
    