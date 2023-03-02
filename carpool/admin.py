from django.contrib import admin

from .models import Post, PostOffer


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)  # connects the models

admin.site.register(PostOffer, PostAdmin)

