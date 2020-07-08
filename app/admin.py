from django.contrib import admin
from .models import User


admin.site.site_header = "Medical Info Website Admin"
admin.site.site_title = "Medical Info Website Admin Area"
admin.site.index_title = "Welcome to the medical info website admin area"

admin.site.register(User)
