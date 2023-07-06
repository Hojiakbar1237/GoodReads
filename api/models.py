from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class  AuthorModel(BaseModel):
    full_name = models.CharField(max_length=50)
    website = models.URLField()
    photo = models.ImageField(upload_to="images/",null=True,blank=True)
    about = models.TextField()

    def __str__(self):
        return f"{self.full_name}"

class BookModel(BaseModel):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(AuthorModel,on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} "