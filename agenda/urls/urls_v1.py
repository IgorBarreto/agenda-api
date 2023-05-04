from django.urls import path

from agenda import views
from rest_framework.routers import SimpleRouter

contato_api_v2_router = SimpleRouter()
contato_api_v2_router.register('agenda/api/v4', views.ContatoAPIV3ViewSet)
app_name = 'agenda_v1'
urlpatterns = [
    path(
        'agenda/api/v1/',
        views.agenda_api_list_v1,
        name='agenda_api_list_v1',
    ),
    path(
        'agenda/api/v1/<int:pk>',
        views.agenda_api_detail_v1,
        name='agenda_api_detail_v1',
    ),
    path(
        'agenda/api/v2/',
        views.ContatoAPIV2List.as_view(),
        name='agenda_api_list_v2',
    ),
    path(
        'agenda/api/v2/<int:pk>',
        views.ContatoAPIV2Detail.as_view(),
        name='agenda_api_detail_v2',
    ),
    path(
        'agenda/api/v3/',
        views.ContatoAPIV3ViewSet.as_view(
            {
                'get': 'list',
                'post': 'create',
            }
        ),
        name='agenda_api_list_v3',
    ),
    path(
        'agenda/api/v3/<int:pk>',
        views.ContatoAPIV3ViewSet.as_view(
            {
                'get': 'retrieve',
                'patch': 'partial_update',
                'delete': 'destroy',
            }
        ),
        name='agenda_api_detail_v3',
    ),
]

urlpatterns += contato_api_v2_router.urls
