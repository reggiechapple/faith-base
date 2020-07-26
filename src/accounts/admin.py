from django.contrib import admin

from .models import Member, Church

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def name(self, obj):
        return obj.user.name


admin.site.register(Member, MemberAdmin)
admin.site.register(Church)