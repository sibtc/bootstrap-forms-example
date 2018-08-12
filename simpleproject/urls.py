from django.urls import path

from people.views import PersonListView, PersonCreateView, PersonUpdateView


urlpatterns = [
    path('', PersonListView.as_view(), name='person_list'),
    path('add/', PersonCreateView.as_view(), name='person_add'),
    path('<int:pk>/edit/', PersonUpdateView.as_view(), name='person_edit'),
]
