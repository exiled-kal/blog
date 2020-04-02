from django.db import models

# Create your models here.
class User(models.Model):
    username = models.TextField()
    
class Blog(models.Model):
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="blogs",blank=True, null=True)
    users_who_liked = models.ManyToManyField(User,related_name="blogs_liked")
    
    
    def __str__(self):
        return f"Blog id {self.id} description: {self.description}"
    
    
    
class BlogEntry(models.Model):
    text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name="entries")
    
class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name="comments")
    blogEntry = models.ForeignKey(BlogEntry,on_delete=models.CASCADE,related_name="comments")