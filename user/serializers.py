from rest_framework import serializers
from .models import Director,Customer,Review
from movie.models import Studio
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class DirectorSerilaizer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    studio_id = serializers.IntegerField()
    studio = serializers.StringRelatedField()
    class Meta:
        model = Director
        fields = '__all__'


class CustomerAuthSerializer(serializers.Serializer):
    token = serializers.SerializerMethodField()
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    password = serializers.CharField(source='user.password',write_only=True)

    def get_token(self,customer):
        token,created = Token.objects.get_or_create(user=customer.user)
        return token.key
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        customer = Customer.objects.create(user=user)
        return customer
    

class DirectorAuthSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    token = serializers.SerializerMethodField()
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    password = serializers.CharField(source='user.password',write_only=True)
    studio = serializers.PrimaryKeyRelatedField(queryset=Studio.objects.all())

    def get_token(self,director):
        token,created = Token.objects.get_or_create(user=director.user)
        return token.key
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        director = Director.objects.create(user=user,**validated_data)
        return director

class AdminAuthSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','token']

    def get_token(self,user):
        token,created = Token.objects.get_or_create(user=user)
        return token.key
    

        

        