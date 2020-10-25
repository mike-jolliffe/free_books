from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple

# Register your models here.
from .models import Book, Author, Location, Author_Book, Location_Book
admin.site.register(Author_Book)
admin.site.register(Location)
admin.site.register(Location_Book)

#pizza = Author and toppings = books

class AuthorAdmin(admin.ModelAdmin):
  filter_horizonal = ('books',)

class BookAdminForm(forms.ModelForm):
  authors = forms.ModelMultipleChoiceField(
    queryset=Author.objects.all(), 
    required=False,
    widget=FilteredSelectMultiple(
      verbose_name=_('Authors'),
      is_stacked=False
    )
  )

  class Meta:
    model = Book
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(BookAdminForm, self).__init__(*args, **kwargs)

    if self.instance and self.instance.pk:
      self.fields['authors'].initial = self.instance.authors.all()

  def save(self, commit=True):
    book = super(BookAdminForm, self).save(commit=False)

    if commit:
      book.save()

    if book.pk:
      book.authors.set(self.cleaned_data['authors'])
      self.save_m2m()

    return book

class BookAdmin(admin.ModelAdmin):
  form = BookAdminForm

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
