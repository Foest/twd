from django.contrib import admin
from dem.models import DemUser, Proposal, Mission

class ProposalAdmin(admin.ModelAdmin):
    list_display = ['title','author', 'date_created']
    prepopulated_fields = {'slug':('title',)}
    fields = ['title', 'content', 'author', 'slug']

class MissionAdmin(admin.ModelAdmin):
    list_display = ['title','creator', 'date_created', 'lat_coord', 'lng_coord']
    prepopulated_fields = {'slug':('title',)}
    fields = ['title', 'creator', 'lat_coord', 'lng_coord', 'description', 'slug']

admin.site.register(DemUser)
admin.site.register(Mission, MissionAdmin)
admin.site.register(Proposal, ProposalAdmin)
