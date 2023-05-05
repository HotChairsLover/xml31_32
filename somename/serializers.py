from rest_framework import serializers
from . import models


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Pr31
        fields = ['title', 'image']


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TodoItem
        fields = '__all__'
