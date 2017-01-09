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


class SessionAdmin(admin.ModelAdmin):
    search_fields=['title','abstract']   

admin.site.register(Sessions,SessionAdmin)





