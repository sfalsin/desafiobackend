from django.contrib import admin
from django.utils.html import format_html
from django.core.paginator import Paginator
from django.core.cache import cache

# Register your models here.

from .models import ImportedUsers

class CachingPaginator(Paginator):
    def _get_count(self):
        return 0#len(self.object_list)
    count = property(_get_count)

class ImpusersModelAdmin(admin.ModelAdmin):
	# A handy constant for the name of the alternate database.
	using = 'impusers'

	def save_model(self, request, obj, form, change):
		obj.save(using=self.using)

	def delete_model(self, request, obj):
		obj.delete(using=self.using)

	def get_queryset(self, request):
		return super().get_queryset(request).using(self.using)

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

	def formfield_for_manytomany(self, db_field, request, **kwargs):
		return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

class ImportedUsersAdmin(ImpusersModelAdmin):
	list_display = ('id','name','login',)
	search_fields = ['name',]
	readonly_fields = ["id"]
	show_full_result_count = False
	ordering = ('priority',)
	#paginator = CachingPaginator
	def get_queryset(self, request):
		qs = super(ImpusersModelAdmin, self).get_queryset(request)
		if 'q' in request.GET:
			param = request.GET.get('q')
			if param:
				return qs
				print(request.GET['q']+' pesquisa')
			else:
				return qs.filter(id=-1)
				print(request.GET['q']+' not pesquisa')
		elif '_changelist_filters' in request.GET:
			return qs
		else:
			return qs.filter(id=-1)
	def has_add_permission(self, request, obj=None):
	        return False
	def get_actions(self, request):
		actions = super().get_actions(request)
		if 'delete_selected' in actions:
			del actions['delete_selected']
		return actions
	def change_view(self, request, object_id, extra_context=None):
	    ''' customize add/edit form '''
	    extra_context = extra_context or {}
	    extra_context['show_save_and_continue'] = False
	    extra_context['show_save'] = False
	    extra_context['show_delete'] = False
	    return super(ImportedUsersAdmin, self).change_view(request, object_id, extra_context=extra_context)

admin.site.register(ImportedUsers,ImportedUsersAdmin)

admin.site.site_header = 'Interface para executar o desafio PicPay - Backend by @sfalsin'
