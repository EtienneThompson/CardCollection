from django.contrib import admin

from .models import Card, Set, Wishlist, Quantity, Collection, User


class CardAdmin(admin.ModelAdmin):
    list_display = ["card_name", "card_set", "card_number", "card_price"]


class SetAdmin(admin.ModelAdmin):
    list_display = ["set_name"]


class WishlistAdmin(admin.ModelAdmin):
    list_display = ["wishlist_id"]


class CollectionAdmin(admin.ModelAdmin):
    list_display = ["collection_name"]


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "auth_token", "last_online", "wishlist"]


admin.site.register(Card, CardAdmin)
admin.site.register(Set, SetAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(User, UserAdmin)
