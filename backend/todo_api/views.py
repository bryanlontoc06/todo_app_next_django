from django.shortcuts import render
from .models import Todo, Author
from .serializers import TodoSerializer, AuthorSerializer
# Generics
from rest_framework import generics

# SessionAuthentication & BasicAuthentication is used for browsers
# BasicAuthentication is not used for production
# TokenAuthentication is used for mobile apps, or desktop applications
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class todoList(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Todo.objects.all()
        author = self.request.query_params.get('author')
        if author is not None:
            queryset = queryset.filter(author=self.request.query_params.get('author'))
        return queryset


class todoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class authorList(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class authorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]