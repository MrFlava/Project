from django.contrib import admin
from main.models import Portfolio, Image, Comment

# Register your models here.


class PortfolioAdmin(admin.ModelAdmin):
    model = Portfolio


class ImageAdmin(admin.ModelAdmin):
    model = Image


class CommentAdmin(admin.ModelAdmin):
    model = Comment


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Comment, CommentAdmin)
