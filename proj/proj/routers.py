from rest_framework import routers
from attachment.viewsets import AttachmentViewSet

router = routers.SimpleRouter()
router.register(r'attachment', AttachmentViewSet, basename='attachment')

