from django.contrib import admin

# Register your models here.

from . models import TeamMember,HeroSection,Service,Portfolio,ContactInfo,Inquiry

admin.site.register(TeamMember)
admin.site.register(HeroSection)
admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(ContactInfo)
admin.site.register(Inquiry)
