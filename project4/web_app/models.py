from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.category_name}"

class Group(models.Model):
    group_name = models.CharField(max_length=100)
    group_price = models.FloatField(default=0,null=True, blank=True)

    def __str__(self):
        return f"{self.group_name} (price: {self.group_price})"

class Colour(models.Model):
    colour_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.colour_name}"

class Photo(models.Model):
    photo_name = models.ImageField()

    def __str__(self):
        return f"{self.photo_name.name}"

class Set(models.Model):
    set_name = models.CharField(max_length=100)
    set_price = models.FloatField(default=0,null=True, blank=True)
    set_colour = models.ManyToManyField(Colour,default='enter_colour' ,null=True, blank=True, related_name='set_colour')
    set_description = models.CharField(max_length=1000, default='enter_description' ,null=True, blank=True)
    set_photo = models.ManyToManyField(Photo, default="add photo", related_name='set_photo', null=True, blank=True)

    def __str__(self):
        return f"{self.set_name} (price: {self.set_price})"

class Items(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.FloatField()
    colour = models.ManyToManyField(Colour, related_name='colour')
    description = models.CharField(max_length=1000)
    category = models.ManyToManyField(Category, related_name='category')
    group = models.ManyToManyField(Group, related_name='group' ,null=True, blank=True)
    sets = models.ManyToManyField(Set, related_name='set' ,null=True, blank=True)
    item_photo = models.ManyToManyField(Photo, related_name='item_photo',default="add photo", null=True, blank=True)

    def __str__(self):
        return f"{self.item_name} (price: {self.price})"
