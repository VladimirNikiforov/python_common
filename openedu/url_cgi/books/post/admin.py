from django.contrib import admin

# Register your models here.

from .models import Post;

class PostModelAdmin(admin.ModelAdmin):
	list_display=["title","tpublish"]
	list_display_links=["tpublish"]
	list_filter=["tpublish"]
	search_fields=["title","content"]
	list_editable=["title"]
	class Meta:
		model=Post


admin.site.register(Post,PostModelAdmin)