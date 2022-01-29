from django.contrib.auth.models import User
from django.db import models

class Todo(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    status=models.CharField(max_length=5,choices=(('new','new'),('done','done')))
    #date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title
    def newga_ozgartir(self):
        self.status="new"
        self.save()
