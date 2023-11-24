from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article,Tag,Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):

        count = 0
        for form in self.forms:

               if form.cleaned_data.get('is_main'):
                   count += 1
                   if count > 1:
                      raise ValidationError('Основной тег должен быть один')
        if count == 0:
                 raise ValidationError('Выберите основной тег')


        return super().clean()




class ScopeInline(admin.TabularInline):
    model = Scope
    extra=3
    formset = ScopeInlineFormset
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title']
    inlines = [ScopeInline]
@admin.register(Tag)
class Tag(admin.ModelAdmin):
    pass








