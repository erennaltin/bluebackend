from django.contrib import admin
from .models import Posts, Approval, Decline, Comment


admin.site.register(Approval)
admin.site.register(Decline)
admin.site.register(Comment)
admin.site.register(Posts)