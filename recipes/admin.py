from django.contrib import admin

# Register your models here.

from .models import Recipe, Author


class VisibleFilter(admin.SimpleListFilter):
    title = 'Visibility'
    parameter_name = 'visible'

    def lookups(self, request, model_admin):
        return [
            ('visible', 'Visible'),
            ('hidden', 'Hidden'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'visible':
            return queryset.filter(visible=True)
        elif self.value() == 'hidden':
            return queryset.filter(visible=False)
        return queryset

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'visible')
    list_filter = (VisibleFilter,)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Author)