from django.contrib import admin
from dem.models import DemUser, Proposal

class ProposalAdmin(admin.ModelAdmin):
    list_display = ['title','author', 'date_created']
    prepopulated_fields = {'slug':('title',)}
    fields = ['title', 'content', 'author', 'slug']

admin.site.register(DemUser)
admin.site.register(Proposal, ProposalAdmin)
