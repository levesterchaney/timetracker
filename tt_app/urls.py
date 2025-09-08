from django.urls import include, path
from rest_framework import routers
from .views import TimesheetViewSet, LineItemViewSet

router = routers.DefaultRouter()
router.register(r'timesheets', TimesheetViewSet, basename="timesheet")
router.register(r'entries', LineItemViewSet, basename="entry")

urlpatterns = [
    path('', include(router.urls))
]