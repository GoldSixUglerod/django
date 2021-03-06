from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="AtomHack",
        default_version='v1',
        description="Swagger for AtomHack",
        license=openapi.License(name="All rights reserved"),
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
    url=settings.BASE_URL,
)
