from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from ..models import Contato
from ..serializers import ContatoSerializer
from rest_framework.views import APIView
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination,
)


# class ContatoAPIV2Pagination(LimitOffsetPagination):
#     default_limit = 10
#     max_limit = 10
# class ContatoAPIV2Pagination(PageNumberPagination):
#     page_size = 2
class ContatoAPIV2Pagination(CursorPagination):
    page_size = 2
    ordering = 'pk'


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


class ContatoAPIV2List(ListCreateAPIView):
    queryset = contatos = Contato.objects.all()
    serializer_class = ContatoSerializer
    # pagination_class = ContatoAPIV2Pagination
    pagination_class = CustomPagination


# class ContatoAPIV2List(APIView):
#     def get(self, request):
#         contatos = Contato.objects.all()
#         serializer = ContatoSerializer(
#             instance=contatos,
#             many=True,
#             context={'request': request},
#         )
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ContatoSerializer(
#             data=request.data,
#             context={'request': request},
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)


class ContatoAPIV2Detail(RetrieveUpdateDestroyAPIView):
    queryset = contatos = Contato.objects.all()
    serializer_class = ContatoSerializer
    # pagination_class = ContatoAPIV2Pagination
    pagination_class = CustomPagination

    # SE PRECISAR UTILIZAR PERSONALIZAR UM METODO
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


# class ContatoAPIV2Detail(APIView):
#     def get_contato(self, pk):
#         contato = get_object_or_404(
#             Contato.objects.filter(),
#             pk=pk,
#         )
#         return contato

#     def get(self, request, pk):
#         contato = self.get_contato(pk)
#         serializer = ContatoSerializer(
#             instance=contato,
#             many=False,
#             context={'request': request},
#         )
#         return Response(serializer.data)

#     def patch(self, request, pk):
#         contato = self.get_contato(pk)
#         serializer = ContatoSerializer(
#             instance=contato,
#             data=request.data,
#             many=False,
#             partial=True,
#             context={'request': request},
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     def delete(self, request, pk):
#         contato = self.get_contato(pk)
#         contato.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
