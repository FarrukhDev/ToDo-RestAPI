from blog.models import Todo
from rest_framework.serializers import ModelSerializer


class TodoSerializer(ModelSerializer):
    class Meta:
        model=Todo
        fields=['title','description','status','user']
