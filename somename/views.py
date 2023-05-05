from defusedxml.ElementTree import fromstring
from django.shortcuts import render
from django.views import View
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_xml.renderers import XMLRenderer
from django.core import serializers
from somename import models, serializers
import requests


class TodoItemList(generics.ListAPIView):
    queryset = models.TodoItem.objects.all()
    serializer_class = serializers.TodoItemSerializer
    renderer_classes = [XMLRenderer]


class TodoItemListHTML(View):

    def get(self, request):
        url = 'http://localhost:8000/todo'
        response = requests.get(url)

        root = fromstring(response.content)
        language_items = root.findall('.//list-item')

        tasks = []
        for item in language_items:
            title = item.find('title').text
            description = item.find('description').text
            due_date = item.find('due_date').text
            due_time = item.find('due_time').text
            task = {'title': title, 'description': description, 'due_date': due_date, 'due_time': due_time}
            tasks.append(task)

        context = {'tasks': tasks}
        return render(request, 'somename/page2.html', context)


class Pr31View(APIView):
    renderer_classes = [XMLRenderer, ]

    def get(self, request):
        languages = models.Pr31.objects.all()
        languages_serializer = serializers.LanguageSerializer(languages, many=True)
        content = {'languages': languages_serializer.data}
        return Response(content)


class Pr31(View):

    def get(self, request):
        url = 'http://localhost:8000/'
        response = requests.get(url)

        root = fromstring(response.content)
        language_items = root.findall('.//list-item')

        languages = []
        for item in language_items:
            title = item.find('title').text
            image = item.find('image').text
            language = {'title': title, 'image': image}
            languages.append(language)

        context = {'languages': languages}
        return render(request, 'somename/page1.html', context)
