from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Subject, SubTopic, Card

def base(request):
    return render(request, 'base.html')

def subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects.html', {'subjects': subjects})

def subject_subtopics(request, name):
    try:
        subject = Subject.objects.get(name=name)
        subtopics = SubTopic.objects.all().filter(subject__name = name )
    except Subject.DoesNotExist:
        raise Http404('SUBJECT NOT FOUND')
    return render(request, 'subject_subtopics.html',{ 'subject': subject, 'subtopics' : subtopics})

def subtopic_cards(request, name, subname):
    try:
        subject = Subject.objects.get(name=name)
        subtopic = SubTopic.objects.get(name= subname)
        cards = Card.objects.all().filter(subTopic__name = subname)
    except Subject.DoesNotExist:
        raise Http404('SUBJECT NOT FOUND')
    return render(request, 'subtopic_cards.html',{ 'subject': subject, 'subtopic' : subtopic, 'cards': cards})

def card(request, name, subname, card):
    try:
        subject = Subject.objects.get(name=name)
        subtopics = SubTopic.objects.all().filter(subject__name = name )
        cards = Card.objects.all().filter(subTopic__name = subname)
        card = cards.get(front = card)
    except Subject.DoesNotExist:
        raise Http404('SUBJECT NOT FOUND')
    return render(request, 'card.html',{ 'subject': subject, 'subtopics' : subtopics, 'card': card})

def test(request, name):
    subject = Subject.objects.get(name=name)
    subtopics = SubTopic.objects.all().filter(subject__name = name )
    cards = []
    for subTopic in subtopics:
        cards += Card.objects.all().filter(subTopic__name = subTopic)
    return render(request, 'test.html', {'subject': subject, 'subtopics': subtopics, 'cards': cards})

def review(request, name):
    subject = Subject.objects.get(name=name)
    subtopics = SubTopic.objects.all().filter(subject__name = name )
    cards = []
    for subTopic in subtopics:
        cards += Card.objects.all().filter(subTopic__name = subTopic)
    return render(request, 'review.html', {'subject': subject, 'subtopics': subtopics, 'cards': cards})
