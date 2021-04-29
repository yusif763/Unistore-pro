from modeltranslation.translator import translator, TranslationOptions

from product.models import (
    Category,
)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('types',)



translator.register(Category, CategoryTranslationOptions)