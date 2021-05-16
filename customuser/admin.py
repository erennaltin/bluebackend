from django.contrib import admin
from .models import Account, UserImage
from django.apps import apps

# admin.site.register(Account)

app = apps.get_app_config('graphql_auth')

for model_name, model in app.models.items():
    admin.site.register(model)
    
class UserImageInline(admin.TabularInline):
    model = UserImage


# admin.site.register(Posts)
# admin.site.register(PostImage)

@admin.register(Account)
class UserAdmin(admin.ModelAdmin):
    inlines = [
        UserImageInline,
    ]