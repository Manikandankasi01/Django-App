from django.contrib import admin
from pdc.models import (
                        PdcForum,
                        PdcMeetingUpdate,
)
# Register your models here.

admin.site.register(PdcForum)
admin.site.register(PdcMeetingUpdate)