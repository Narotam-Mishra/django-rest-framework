from rest_framework import permissions
from .permissions import IsDevEditorPemission

class StaffEditorPermissionMixin():
    permissions_classes = [permissions.IsAdminUser, IsDevEditorPemission]