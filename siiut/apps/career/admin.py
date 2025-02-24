from django.contrib import admin

from .models import Career, Subject, Level, Quarter

admin.site.register(Level)
admin.site.register(Quarter)
#admin.site.register(Career)
#admin.site.register(Subject)

class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 5

@admin.register(Career)
class CareerModelAdmin(admin.ModelAdmin):
    list_fields = ['id', 'level', 'name', 'is_active', 'principal']
    list_filter = ['level']
    fields = ['short_name', 'level', 'name', 'principal']
    inlines = [SubjectInline]