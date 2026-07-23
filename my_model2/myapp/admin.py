from django.contrib import admin
from .models import Student

# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
   list_display = ('name', 'email')
   list_filter = ('email', 'name')
   search_fields = ('name', 'email')
   list_editable = ('email',)
    