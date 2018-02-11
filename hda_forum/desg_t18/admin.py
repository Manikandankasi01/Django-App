from django.contrib import admin
from desg_t18.models import (UserInformation,
                            DesgT18WorkFlow,
                            TriageNote,
                            KnowledgeSharing,
                            OverView,
                            MeetingUpdate,
                            DesgPcUpdate,
                            DesgGmlUpdate,
                            )
# Register your models here.

admin.site.register(UserInformation)
admin.site.register(DesgT18WorkFlow)
admin.site.register(TriageNote)
admin.site.register(KnowledgeSharing)
admin.site.register(OverView)
admin.site.register(MeetingUpdate)
admin.site.register(DesgPcUpdate)
admin.site.register(DesgGmlUpdate)
