from r2.lib.pages import BoringPage, WrappedUser

class ModCardPage(BoringPage):
    def __init__(self, user, **kw):
        self.user = user
        self.wrappeduser = WrappedUser(user)
        self.permissions = kw.pop('permissions')
        self.is_moderator = kw.pop('is_moderator')
        self.mod_permissions = None
        if self.is_moderator:
            self.mod_permissons = ModeratorPermissions(self.user,
                "moderator", self.permissions, embedded=True)
        BoringPage.__init__(self, user.name, **kw)
