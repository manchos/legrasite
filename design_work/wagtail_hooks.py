from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import DesignWorkPage


class InteriorDesignPageAdmin(ModelAdmin):
    model = DesignWorkPage
    menu_label = 'Интерьеры'  # ditch this to use verbose_name_plural from model
    menu_icon = 'date'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('title', 'body', 'sequence_number', 'design_kind')
    list_filter = ('title',)
    search_fields = ('title',)
    # ordering = ['sequence_number']
    list_per_page = 12

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     # Only show people managed by the current user
    #     return qs.filter(design_kind=1)

# Now you just need to register your customised ModelAdmin class with Wagtail


class GraphicDesignPageAdmin(ModelAdmin):
    model = DesignWorkPage
    menu_label = 'Графический дизайн'  # ditch this to use verbose_name_plural from model
    menu_icon = 'date'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('title', 'body', 'sequence_number', 'design_kind')
    list_filter = ('title',)
    search_fields = ('title',)
    ordering = ['sequence_number']
    list_per_page = 12

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Only show people managed by the current user
        return qs.filter(design_kind=2)

modeladmin_register(InteriorDesignPageAdmin)

# modeladmin_register(GraphicDesignPageAdmin)
