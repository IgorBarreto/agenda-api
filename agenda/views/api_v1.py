from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Contato
from ..serializers import ContatoSerializer


# FBV
@api_view(http_method_names=['get', 'post'])
def agenda_api_list_v1(request):
    if request.method == 'GET':
        contatos = Contato.objects.all()
        serializer = ContatoSerializer(
            instance=contatos,
            many=True,
            context={'request': request},
        )
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ContatoSerializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['get', 'pathc', 'delete'])
def agenda_api_detail_v1(request, pk):
    contato = get_object_or_404(
        Contato.objects.filter(),
        pk=pk,
    )
    if request.method == 'GET':
        serializer = ContatoSerializer(
            instance=contato,
            many=False,
            context={'request': request},
        )
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = ContatoSerializer(
            instance=contato,
            data=request.data,
            many=False,
            partial=True,
            context={'request': request},
        )
        return Response(serializer.data)
    elif request.method == 'DELETE':
        contato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
