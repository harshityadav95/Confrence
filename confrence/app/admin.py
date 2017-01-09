from django.contrib import admin
from app.models import *



# for changing Site Header  
admin.site.site_header = 'Confrence Scheduler'
admin.site.site_title="Administration"


#create List View For Speaker Class  
class SpeakerAdmin(admin.ModelAdmin):
    list_display=('name','bio')



# Register your models here.
admin.site.register(Track)
admin.site.register(Speaker,SpeakerAdmin)

# Search Box in Sessions Field 


class SessionAdmin(admin.ModelAdmin):
    list_display=('title','speaker')
    search_fields=['title','abstract']   
    list_filter=('track__title','speaker')


admin.site.register(Sessions,SessionAdmin)





