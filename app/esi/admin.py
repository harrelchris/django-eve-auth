from django.contrib import admin

from esi.models import Alliance
from esi.models import Character
from esi.models import Corporation


class AllianceAdmin(admin.ModelAdmin):
    pass


class CharacterAdmin(admin.ModelAdmin):
    pass


class CorporationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Alliance, AllianceAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Corporation, CorporationAdmin)
