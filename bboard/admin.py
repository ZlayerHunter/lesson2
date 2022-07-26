from django.contrib import admin

# Register your models here.

from.models import Bb, Rubric

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title',)
    search_fields = ('title', 'content', 'price')
    
#class RubricAdmin(admin.ModelAdmin):
    #list_display = ('name',)

admin.site.register(Bb, BbAdmin)
#admin.site.register(Rubric, RubricAdmin)
admin.site.register(Rubric)