from django.urls import path

from activitylogs.api.views import ActivityLogView


urlpatterns = [
    path('activity-log-create/', ActivityLogView.as_view(), name='activity-log-create'),
]
