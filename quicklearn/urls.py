
from django.contrib import admin
from django.urls import path

from indexcards import views

urlpatterns = [
    path('', views.subjects, name='subjects'),
    path('admin/', admin.site.urls),
    path('subjects/', views.subjects, name='subjects'),
    path('subjects/<name>/', views.subject_subtopics, name='subject_subtopics'),
    path('subjects/<name>/test', views.test, name='test'),
    path('subjects/<name>/review', views.review, name='review'),
    path('subjects/<name>/<subname>/', views.subtopic_cards, name='subtopic_cards'),
    # path('subjects/<name>/<subname>/test', views.test, name='test'),
    # path('subjects/<name>/<subname>/review', views.review, name='review'),
    path('subjects/<name>/<subname>/<card>', views.card, name='card'),

]
