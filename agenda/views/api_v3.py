from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from ..models import Contato
from ..serializers import ContatoSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination,
)


class CustomPagination(PageNumberPagination):
    page_size = 2

    def get_paginated_response(self, data):
        return Response(
            {
                'proximo': self.get_next_link(),
                'anterior': self.get_previous_link(),
                'total': self.page.paginator.count,
                'dados': data,
            }
        )


class ContatoAPIV3ViewSet(ModelViewSet):
    queryset = contatos = Contato.objects.all()
    serializer_class = ContatoSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        qs = super().get_queryset()
        tipo_telefone = self.request.query_params.get('tipo_telefone', None)
        if tipo_telefone is not None:
            qs = qs.filter(tipo_telefone=tipo_telefone)
        return qs

    def partial_update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        contato = self.get_queryset().filter(pk=pk).first()
        serializer = ContatoSerializer(
            instance=contato,
            data=request.data,
            context={'request': request},
            many=False,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
