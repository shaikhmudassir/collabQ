from django.contrib import admin
from .models import Issue, Assign

class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'complexity', 'deadline', 'raised_by', 'status', 'created_at')
admin.site.register(Issue, IssueAdmin)

class AssignAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'issue_id')
admin.site.register(Assign, AssignAdmin)