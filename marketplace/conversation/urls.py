from django.urls import path

from . import views

app_name = "conversation"

urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("new/<int:pk>/", views.new_conversation, name="new"),
    path("<int:pk>/", views.detail, name="detail"),
]