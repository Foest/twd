from django.contrib import admin
from dem.models import DemUser, Proposal, Mission, Reward, Assignment

class ProposalAdmin(admin.ModelAdmin):
    list_display = ['title','author', 'date_created']
    prepopulated_fields = {'slug':('title',)}
    fields = ['title', 'content', 'author', 'slug']

class MissionAdmin(admin.ModelAdmin):
    list_display = ['title','creator', 'date_created']
    prepopulated_fields = {'slug':('title',)}
    fields = ['title', 'creator', 'description', 'slug']

class RewardAdmin(admin.ModelAdmin):
    list_display = ['title', 'monies']
    fields = ['title', 'monies']

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['assignee', 'mission', 'reward', 'lat_coord', 'lng_coord']
    fields = ['assignee', 'mission', 'reward', 'lat_coord', 'lng_coord']

admin.site.register(DemUser)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Reward, RewardAdmin)
admin.site.register(Mission, MissionAdmin)
admin.site.register(Proposal, ProposalAdmin)
