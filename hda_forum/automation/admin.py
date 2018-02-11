from django.contrib import admin
from automation.models import (
							DesgAutomationRelease,
							DesgAutomationUpdate,
 							PdcAutomationUpdate,
                            PdcAutomationRelease,
							LdmAutomationUpdate,
                            LdmAutomationRelease,
                            )
# Register your models here.
admin.site.register(DesgAutomationUpdate)
admin.site.register(DesgAutomationRelease)
admin.site.register(PdcAutomationUpdate)
admin.site.register(PdcAutomationRelease)
admin.site.register(LdmAutomationUpdate)
admin.site.register(LdmAutomationRelease)