from django.urls import path

from agenda import views

app_name = 'agenda'
urlpatterns = [
    path(
        'agenda/api/v1/',
        views.agenda_api_list,
        name='agenda_api_v2',
    ),
    path(
        'agenda/api/v1/<int:pk>/',
        views.agenda_api_detail,
        name='agenda_api_v2_detail',
    ),
]
