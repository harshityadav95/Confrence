from django.contrib import admin
from app.models import *



# for changing Site Header  
admin.site.site_header = 'Confrence Scheduler'
admin.site.site_title="Administration"

# Register your models here.
admin.site.register(Track)
admin.site.register(Speaker)
admin.site.register(Sessions)





