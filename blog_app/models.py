from django.db import models

class Blog(models.Model):
    author = models.ForeignKey("auth.user",on_delete=models.CASCADE)
    topics = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    