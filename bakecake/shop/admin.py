from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from shop.models import AppUser, BakeCakeLevels, BakeCakeShape, BakeCake, BakeCakeTopping, BakeCakeBerries, \
    BakeCakeDecor, Catalog


@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    ...


@admin.register(BakeCakeLevels)
class BakeCakeLevelsAdmin(admin.ModelAdmin):
    ...


@admin.register(BakeCakeShape)
class BakeCakeShapeAdmin(admin.ModelAdmin):
    ...


@admin.register(BakeCakeTopping)
class BakeCakeToppingAdmin(admin.ModelAdmin):
    ...


@admin.register(BakeCakeBerries)
class BakeCakeBerriesAdmin(admin.ModelAdmin):
    ...


@admin.register(BakeCakeDecor)
class BakeCakeDecorAdmin(admin.ModelAdmin):
    ...


@admin.register(BakeCake)
class BakeCakeAdmin(admin.ModelAdmin):
    ...


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

    readonly_fields = ('slug', )
