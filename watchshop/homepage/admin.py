from django.contrib import admin
from .models import Watches,WatchUpload,Wishlist,Cart,CartItem,WatchReview
# Register your models here.
admin.site.register(Watches)


#WatchUploads
class WatchUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'image')
    list_filter = ('name', 'price')
    search_fields = ['name', 'description']

admin.site.register(WatchUpload, WatchUploadAdmin)

admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(CartItem)


#WatchReview
class WatchReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'review_text', 'rating')
    list_filter = ('rating', 'product')
admin.site.register(WatchReview, WatchReviewAdmin)