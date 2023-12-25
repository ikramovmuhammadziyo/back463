from django.db import models


class CaruselModel(models.Model):
    photo = models.ImageField(upload_to="foods")
    desc = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.desc} | {self.created_at}"


class LeftMenuModel(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to="menu")
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} | {self.created_at}"


class RightMenuModel(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to="menu")
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} | {self.created_at}"


class GalleryModel(models.Model):
    photo = models.ImageField(upload_to="gallery")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.photo} | {self.created_at}"


class RESERVATIONModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} | {self.created_at}"

