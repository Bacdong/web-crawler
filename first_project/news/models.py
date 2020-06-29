from django.db import models

class Reporter(models.Model):
    fullName = models.CharField(max_length = 40)

    def __str__(self):
        return self.fullName

class Article(models.Model):
    pub_date = models.DateField()
    headLine = models.CharField(max_length = 255)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete = models.CASCADE)

    def __str__(self):
        return self.headLine