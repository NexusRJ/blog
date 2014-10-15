from django.db import models
from django.contrib import admin
from DjangoUeditor.models import UEditorField


class Archives(models.Model):
    title = models.CharField(max_length=150)
    content = UEditorField()
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
    list_display = ('title', 'id', 'timestamp')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('archivetitle','id', 'content', 'author')

admin.site.register(Archives,ArchivesAdmin)
admin.site.register(Comments,CommentsAdmin)
