from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255, verbose_name="Document Title")
    authors = models.TextField(verbose_name="Authors", help_text="List of authors, separated by commas")
    upload_date = models.DateTimeField(auto_now_add=True, verbose_name="Upload Date")
    file_path = models.FileField(upload_to='documents/', verbose_name="Document File")
    abstract = models.TextField(blank=True, null=True, verbose_name="Abstract/Summary")

    def __str__(self):
        return self.title
