from django.shortcuts import render
from django.http import JsonResponse
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins


# Class based view
# class BookList(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)

# Class based view with mixin
class BookList(mixins.ListModelMixin,  generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# class BookCreate(APIView):
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Using mixin
class BookCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class BookDetails(APIView):
#     def get_book_by_pk(self, pk):
#         try:
#             return Book.objects.get(pk=pk)
#         except:
#             return Response({
#                 'error': 'Books does not found'
#             }, status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, pk):
#         book = self.get_book_by_pk(pk)
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         book = self.get_book_by_pk(pk)
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         book = self.get_book_by_pk(pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# using mixins
class BookDetails(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



# Create your views here.
# @api_view(['GET'])
# def book_list(request):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def book_create(request):
#     serializer = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def book(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except:
#         return Response({
#             'error': 'Books does not found'
#         }, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
#
#     if request.method == 'PUT':
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
