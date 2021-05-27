from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "Poll App"
admin.site.site_title = "Poll App area"
admin.site.site_title = "Welcome to the Poll App admin area"
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]   
    inline = [ChoiceInline]  



# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
