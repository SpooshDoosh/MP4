from django.db import models

# Create your models here.


class BlogMod(models.Model):
    id = models.IntegerField(primary_key=True)
    blog_title = models.CharField(max_length=30)
    blog = models.TextField()

    def __str__(self):
        return f'Blog: {self.blog_title}'


class CommentMod(models.Model):
    your_name = models.CharField(max_length=30)
    comment_body = models.TextField()
    blog = models.ForeignKey('BlogMod', on_delete=models.CASCADE)

    def __str__(self):
        return f'Commented by {self.your_name}'
