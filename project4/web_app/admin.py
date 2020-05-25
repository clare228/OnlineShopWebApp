from django.contrib import admin

from .models import Items, Category, Group, Colour, Set

class ItemsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class GroupAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class ColourAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class SetAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


# Register models
admin.site.register(Items, ItemsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Colour, ColourAdmin)
admin.site.register(Set, SetAdmin)





