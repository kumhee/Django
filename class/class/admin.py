from django.contrib import admin
from .models import Choice, Question

# class ChoiceAdmin(admin.ModelAdmin): 
#     fields = ('choice_text', 'votes', 'question')
    
class ChoiceAdmin(admin.ModelAdmin): 
    fieldsets = (
        ('Choice', {'fields' : ('choice_text', 'votes')}),
        ('Question', {'fields' : ('question',)})
    )
    list_display = ('choice_text', 'question')
    list_filter = ('choice_text',)  
    search_fields = ('choice_text',)

admin.site.register(Question)
admin.site.register(Choice, ChoiceAdmin)