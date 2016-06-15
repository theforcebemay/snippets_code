# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    # list all or create one more
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
























# @csrf_exempt
# def snippet_list(request):
#     '''
#     list of all snippets, or create a new one
#     '''
#     if request.method == 'GET':
#         snippets = Snippet.objects.all() # собрать все данные с БД в переменную
#         serializer = SnippetSerializer(snippets, many=True) # с помощью сериалайзеров, которые мы написали в serializers.py делаем инстанс сериалайзер
#         return JSONResponse(serializer.data) # serializer это сериализированые данные. JSONResponse отдает метод .data инстанса serializer. Вдумайся
#
#     # Чтобы отдать инфу, GET:
#     # 1.Cначала собрать с помощью Джанго ОРМ все обьекты в одну переменную
#     # 2.Эту переменную сериализировать и сделать инстанс.
#     # 3.Отдать переменную в JSONе
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request) # мы конвертируем request (который пришел) в переменную data, прежде конвертируя ее в JSON
#         serializer = SnippetSerializer(data=data) # С  помощью нашего сериалайзера(serializers.py) мы делаем инстанс в переменную serializer
#         if serializer.is_valid(): # проверяем валидность сериалайзера, если все ок, мы его сохраняем и возвращаем .data в JSON формате
#             serializer.save()
#             return JSONResponse(serializer.data, status=201) # возврат данных
#         return JSONResponse(serializer.errors, status=400) # если что то не так, мы отдаем отчет об ошибках и статус 400
#
#     # Чтобы сделать POST:
#     # 1. Сначала сделаем парсинг request и с помощью JSONParser сохраним его в переменную data
#     # 2. После этого сериализировать в переменную, с заменой .data на новую(которая пришла с request)
#     # 3. Если data пришла праильная(serializator.is_valid), то сохраняем serializer (serializer.save()), и возвращаем назад сохраненные данные, в другом случае, отдаем 400 статус и отчет об ошибках.
#
#
# @csrf_exempt
# def snippet_detail(request, pk):
#     try:
#         snippet = Snippet.objects.get(pk=pk) #  шукаємо в БД об’єкт з ключем вказаним у запиті, якщо його немає, відправляємо помилку 404
#     except Snippet.DoesNotExist: # якщо все ж існує, тоді прив’язуємо об’єкт до перемінної snippet
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)
#
