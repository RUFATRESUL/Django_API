from rest_framework import serializers
from .models import Studio,Genre,Movie
from user.serializers import DirectorSerilaizer
from user.models import Director, Review



class StudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Studio
        fields = '__all__'



class GenreSerializer(serializers.ModelSerializer):
     
     class Meta:
        model = Genre
        fields = '__all__'
        # fields = ['id','title','update'] # eyni anda 3 fields getirir
        # exclude = ['update'] # update create evez edir


class MovieSerializer(serializers.ModelSerializer):
    director_info = DirectorSerilaizer(source="director", read_only=True) # yazdigimiz 2 setir kod bize director melumatlarini object seklinde getirir yazmadiqda null qaytarir
    studio = serializers.CharField(source='director.studio.title', read_only=True)
    # director = serializers.PrimaryKeyRelatedField(queryset=Director.objects.all(),write_only=True)
    genres_info = GenreSerializer(many=True, source='genres', read_only=True) #janrlari id seklinde deyil object seklinde getirir extra_kwargs ile birlikde
    class Meta:
        model = Movie
        exclude = ['director']
        extra_kwargs = {
            'genres': {'write_only': True},
        }

    def validate_title(self,value):
        if not value.istitle():
            raise serializers.ValidationError('Title must be capitalized')
        return value
        
    def validate(self, data):
        if "title" in data and "description" in data and data['title'] in data['description']:
            raise serializers.ValidationError("Title can't be used in description")
        return data
    
    def create(self, validated_data):
        director = self.context['request'].user.director
        genres = validated_data.pop('genres')
        movie = Movie.objects.create(director=director,**validated_data)
        movie.genres.set(genres)
        movie.save()
        return movie
    
class BlogCommentSerializer(serializers.Serializer):
   
    class Meta:
        model = Review
        fields = '__all__'
    
        

    

