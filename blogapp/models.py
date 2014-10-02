from django.db import models
from django.contrib import admin
from DjangoUeditor.models import UEditorField


class Archives(models.Model):
    title = models.CharField(max_length=150)
    body = UEditorField('body')
    timestamp = models.DateField()
    archivetype = models.CharField(max_length=150, default='books')

    class Meta:
        ordering = ('-timestamp', 'title', 'archivetype', 'id')


class ArchivesAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'archivetype', 'body')



admin.site.register(Archives,ArchivesAdmin)
