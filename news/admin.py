from django.contrib import admin
from .models import User, Category, Subcategory, Subscription, News

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
        # Remove the unwanted fields from the admin form
    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )

    # Remove the unwanted fields from the add form
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("phone_number", "password1", "password2"),
        }),
    )

    # Remove the unwanted fields from the change form
    readonly_fields = ("username",)

    # Set the list display to show the desired fields
    list_display = ("phone_number", "is_staff", "is_active")

    # Set the search fields to enable searching by phone number
    search_fields = ("phone_number",)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    ordering = ['category', 'name']

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'subcategory', 'start_date', 'is_active']
    ordering = ['user', 'subcategory']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'subcategory', 'publish_date']
    ordering = ['-publish_date']
