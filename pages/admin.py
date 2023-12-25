from django.contrib import admin

from pages.models import CaruselModel, LeftMenuModel, RightMenuModel, GalleryModel, RESERVATIONModel

admin.site.register(RESERVATIONModel)
admin.site.register(GalleryModel)
admin.site.register(RightMenuModel)
admin.site.register(LeftMenuModel)
admin.site.register(CaruselModel)
