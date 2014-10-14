from django.db import models
from django.contrib import admin
from DjangoUeditor.models import UEditorField


class Archives(models.Model):
    title = models.CharField(max_length=150)
    body = UEditorField('body')
    timestamp = models.DateField()
    archivetype = models.CharField(max_length=150, default='books')

    class Meta:
        ordering = ('-timestamp',)


class Comments(models.Model):
    archiveid = models.ForeignKey(Archives)
    archivetitle = models.TextField(max_length=150)
    content = models.TextField(max_length=300)
    author = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    link = models.URLField(max_length=100, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)


class ArchivesAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'archivetype', 'body')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'author', 'archivetitle')

admin.site.register(Archives,ArchivesAdmin)
admin.site.register(Comments,CommentsAdmin)