from django.contrib import admin
from somename import models


@admin.register(models.Pr31)
class Pr31Admin(admin.ModelAdmin):
    pass


@admin.register(models.TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    pass
