from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from product.models import(
    Tag,
    Product,
    ProductSpecName,
    ProductSpecDesc,
    Brands,
    Category,
    ScreenSize,
    Review,
    Image,
    ShortSpec,
)

class ImageTabularInline(admin.TabularInline):
    model = Image
    list_display = ('image',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tags','created_at')
    list_filter = ('tags',)
    search_fields = ('tags',)
@admin.register(ShortSpec)
class TagAdmin(admin.ModelAdmin):
    list_display = ('short_specs','created_at')
    list_filter = ('short_specs',)
    search_fields = ('short_specs',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageTabularInline,]
    list_display = ('full_title','price','created_at')
    list_filter = ('full_title','price')
    search_fields = ('price','price',)

@admin.register(ProductSpecName)
class ProductSpecNameAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')
    list_filter = ('title',)
    search_fields = ('title',)

@admin.register(ProductSpecDesc)
class ProductSpecDescAdmin(admin.ModelAdmin):
    list_display = ('desc','created_at')
    list_filter = ('desc',)
    search_fields = ('desc',)

@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('brand','created_at')
    list_filter = ('brand',)
    search_fields = ('brand',)


class CategoryAdmin(TranslationAdmin):
    list_display = ('id', 'types', 'created_at')

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('types','created_at')
#     list_filter = ('types',)
#     search_fields = ('types',)

@admin.register(ScreenSize)
class ScreenSizeAdmin(admin.ModelAdmin):
    list_display = ('size','created_at')
    list_filter = ('size',)
    search_fields = ('size',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','comment','created_at')
    list_filter = ('full_name','email','comment','created_at')
    search_fields = ('full_name','email',)



admin.site.register(Category,CategoryAdmin)

# admin.site.register([Product,ProductSpecName,Category,ProductSpecDesc,ScreenSize,Brands,Review])