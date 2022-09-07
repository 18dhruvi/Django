from django.contrib import admin
from members.models import Profile,BlogPost,Comment,User

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(BlogPost)
admin.site.register(Comment)

