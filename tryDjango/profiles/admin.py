from django.contrib import admin

# Register your models here.
from .models import profile

class profileAdmin(admin.ModelAdmin):
	"""docstring for profileAdmin"""
	class Meta(object):
		model = profile


admin.site.register(profile, profileAdmin)

			
		