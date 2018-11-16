from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "- ( id: " + str(self.id) + ", user 1st name: " + self.first_name + ", user last name: " + self.last_name + ", user email: " + self.email + " ) -"

class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.CharField(max_length = 255)
    uploader = models.ForeignKey(User, related_name = "uploaded_books")
    liked_users = models.ManyToManyField(User, related_name = "liked_books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "- ( id: " + str(self.id) + ", book name: " + self.name + ", book description: " + self.desc + " ) -"