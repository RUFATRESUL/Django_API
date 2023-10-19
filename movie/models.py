from django.db import models


class Studio(models.Model):
    title = models.CharField(max_length=100)
    update = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class Genre(models.Model):
    title = models.CharField(max_length=100)
    update = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    



class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    released = models.DateField()
    # imdb = models.IntegerField()
    # studio = models.ForeignKey(Studio, on_delete=models.SET_NULL,null=True,blank=True)
    image = models.ImageField(upload_to='movie/images',blank=True,null=True)
    director = models.ForeignKey('user.Director', on_delete=models.SET_NULL,null=True,blank=True)
    genres = models.ManyToManyField(Genre)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    


