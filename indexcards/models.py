from django.db import models
# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return (self.name)

class SubTopic(models.Model):
    name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return (self.name)

class IndexCard(models.Model):
    front = models.CharField(max_length=50)
    back = models.CharField(max_length=100)
    subTopic = models.ForeignKey(SubTopic, on_delete=models.CASCADE)

    def __str__(self):
        return (self.name)

class Card(models.Model):
    front = models.CharField(max_length=50)
    back = models.CharField(max_length=100)
    subTopic = models.ForeignKey(SubTopic, on_delete=models.CASCADE)

    def __str__(self):
        return (self.front)
