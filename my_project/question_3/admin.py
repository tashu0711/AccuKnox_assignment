from django.contrib import admin
from .models import UserProfile, ActivityLog

admin.site.register(UserProfile)
admin.site.register(ActivityLog)

#importnat note --> superuser username :: ACCUKNOX_F(isi se login krna hai nhin to error aaega)
# email :: cs21b007@iittp.ac.in
# password :: ashu()09;