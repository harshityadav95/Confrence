from django.contrib import admin
from app.models import *



# for changing Site Header  
admin.site.site_header = 'Confrence Scheduler'
admin.site.site_title="Administration"


#create List View For Speaker Class  
class SpeakerAdmin(admin.ModelAdmin):
    list_display=('name','bio')

    # adding Collapsable and Grouped Menu  
    fieldsets=(
        ("Genral Information",
            {
                "fields":('name','bio',)
             }
         ),
        (
            "Social Media",
            {
             "classes":("collapse",),
             "fields":('twitter','facebook'),
             "description":"Add Social Media Here"

                         })
        )



# Register your models here.
admin.site.register(Track)
admin.site.register(Speaker,SpeakerAdmin)

# Search Box in Sessions Field 


class SessionAdmin(admin.ModelAdmin):
    list_display=('title','status')
    search_fields=['title','abstract']   
    list_filter=('track__title','speaker')
    
    # Calling of the Actions Mark Approved Defination 
    actions=['make_approved',]

    # function to perform action on selected fields  
    def make_approved(self,request,queryset):
        rows_updated=queryset.update(status='a')
        if rows_updated==1:
            message_bit='1 session was'
        else:
            message_bit='%s sessions were'%rows_updated

            #Displaying User Error Message 
        self.message_user(request,'%s approved.'%message_bit)

        #Message to appear in the  Drop-Down  Actions Menu  
    make_approved.short_description='Mark sessions(s) as approved'




admin.site.register(Sessions,SessionAdmin)





