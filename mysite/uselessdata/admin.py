from django.contrib import admin
from uselessdata.models import Blogs, Comments, Contacts

# Register your models here.

admin.site.register(Blogs)
admin.site.register(Comments)
admin.site.register(Contacts)