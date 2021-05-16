from django.contrib import admin
from .models import Posts, PostImage, Approval, Decline, Comment


class PostImageInline(admin.TabularInline):
    model = PostImage


admin.site.register(Approval)
admin.site.register(Decline)
admin.site.register(Comment)


@admin.register(Posts)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        PostImageInline,
    ]