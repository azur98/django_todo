from django.db import models


class TodoModel(models.Model):

    title = models.CharField(max_length=100)

    content = models.TextField(max_length=1000,null=True)

    pic = models.ForeignKey('auth.User', on_delete=models.CASCADE)