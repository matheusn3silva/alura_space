from django.contrib import admin
from galeria.models import Photograph

class listingPhotographs(admin.ModelAdmin):
    list_display = ("id", "name", "legend")
    list_display_links = ("id", "name")
    search_fields = ("name",)

admin.site.register(Photograph, listingPhotographs)
