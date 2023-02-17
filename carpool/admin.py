from django.contrib import admin
from .models import Post
from .models import Question
# from .models import Matches
# from .models import Offers
# from .models import Requests

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Question)
