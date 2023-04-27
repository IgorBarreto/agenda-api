from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from agenda.models import Contato
from agenda.serializers import ContatoSerializer
from rest_framework import status


# Create your views here.
@api_view(http_method_names=['get', 'post'])
def agenda_api_list(request):
    if request.method == 'GET':
        contatos = Contato.objects.all()
        serializer = ContatoSerializer(
            instance=contatos,
            many=True,
            context={
                'request': request,
            },
        )
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ContatoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


@api_view(http_method_names=['get', 'patch', 'delete'])
def agenda_api_detail(request, pk):
    contato = get_object_or_404(Contato.objects, pk=pk)
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
            many=False,
            data=request.data,
            partial=True,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        contato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
