from django.contrib import admin

from .models import Subject, SubTopic, Card

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(SubTopic)
class SubTopicAdmin(admin.ModelAdmin):
    list_display =['name', 'subject']

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['front', 'back','subTopic']
