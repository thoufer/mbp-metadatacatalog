from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from taggit.admin import Tag

from .models import Asset, Organization, TaggedSubject, TaggedPlace, SubjectTag, LocationTag

admin.site.register(Asset, SimpleHistoryAdmin)
admin.site.register(TaggedSubject)
admin.site.register(TaggedPlace)
admin.site.register(SubjectTag)
admin.site.register(LocationTag)

admin.site.unregister(Tag)

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("code", "region", "name")
    readonly_fields = ("region",)

admin.site.register(Organization, OrganizationAdmin)
