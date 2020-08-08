from django.contrib import admin

from .models import Member, Cleric

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def name(self, obj):
        return obj.user.name

class ClericAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def name(self, obj):
        return obj.user.name


admin.site.register(Member, MemberAdmin)
admin.site.register(Cleric, ClericAdmin)