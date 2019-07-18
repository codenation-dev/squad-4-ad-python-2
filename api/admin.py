from django.contrib import admin
from api.models.sale import Sale
from api.models.seller import Seller
from api.models.plan import Plan


class CustomModelAdminMixin(object):
    """
    Thanks to: https://stackoverflow.com/a/28255245
    """
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(CustomModelAdminMixin, self).__init__(model, admin_site)


class SaleAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass


class SellerAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass


class PlanAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass


admin.site.register(Sale, SaleAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Plan, PlanAdmin)
