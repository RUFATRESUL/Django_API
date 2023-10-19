from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate
from rest_framework import generics,decorators,status,serializers
from rest_framework.response import Response
from .serializers import DirectorSerilaizer,CustomerAuthSerializer,DirectorAuthSerializer,AdminAuthSerializer
from .models import Director, Review
from .thorttlings import Anon5ForMinute, User10ForMinute
from movie.models import Movie



# Create your views here.

class DirectorListAV(generics.ListCreateAPIView):
    serializer_class = DirectorSerilaizer
    queryset = Director.objects.all()


class DirectorDetailAV(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DirectorSerilaizer
    queryset = Director.objects.all()


@decorators.api_view(['POST'])
@decorators.throttle_classes([Anon5ForMinute,])
def customer_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username,password=password)
    if user and hasattr(user,'customer'):
        serializer = CustomerAuthSerializer(user.customer)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@decorators.api_view(['POST'])
def customer_register(request):
    serializer = CustomerAuthSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    

@decorators.api_view(['POST'])
@decorators.throttle_classes([Anon5ForMinute,])
def director_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username,password=password)
    if user and hasattr(user,'director'):
        serializer = DirectorAuthSerializer(user.director)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@decorators.api_view(['POST'])
def director_register(request):
    serializer = DirectorAuthSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    

@decorators.api_view(['POST'])
def admin_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username,password=password)
    if user and user.is_superuser:
        serializer = AdminAuthSerializer(user)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# class BlogCommentListCreateAV(generics.ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = BlogCommentSerializer

#     def get_queryset(self):
#         movie_pk = self.kwargs.get('movie_pk')
#         return Review.objects.filter(movie__title=movie_pk)
    
#     def perform_create(self,serializer):
#         movie_pk = self.kwargs.get('movie_pk')
#         movie_review =get_object_or_404(Movie,pk=movie_pk)
#         if Review.objects.filter(movie=movie_review, customer=self.request.user).exists():
#             raise serializers.ValidationError({'detail':'You have already added comment on this movie'})
#         serializer.save(customer=self.request.user, movie=movie_review)
        

# class BlogCommentListCreateAV(generics.CreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = BlogCommentSerializer

#     def create(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
#     def perform_create(self,serializer):
#         movie_pk = self.kwargs.get('title')
#         movie =get_object_or_404(Movie,pk=movie_pk)
#         serializer.save(movie=movie)

# class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = BlogCommentSerializer
        


