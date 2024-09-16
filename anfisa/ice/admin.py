from django.contrib import admin

from .models import Level, LevelPrize, Player, PlayerLevel, Prize


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk',)


admin.site.register(Player, PostAdmin)
admin.site.register(Level)
admin.site.register(Prize)
admin.site.register(LevelPrize)
admin.site.register(PlayerLevel)
