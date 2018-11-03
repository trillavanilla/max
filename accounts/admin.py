from django.contrib import admin
from accounts.models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'info', 'location', 'site')

    def info(self, obj):
        return obj.description

    def location(self, obj):
        return obj.city

    def site(self, obj):
        return obj.website

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-user')
        return queryset

admin.site.register(UserProfile, UserProfileAdmin)
