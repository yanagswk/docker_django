from django.contrib import admin
from .models import Journal, Category, Tag, Comment, Reply

admin.site.register(Journal)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Reply)



