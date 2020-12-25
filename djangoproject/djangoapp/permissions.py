from rest_framework.permissions import IsAdminUser

class IsAdminUserForRetrieve(IsAdminUser):

    def has_permission(self, request, view):
        if view.action == 'retrieve':
            if request.user.is_staff:
                return True
            else:
                return False
        else:
            return True