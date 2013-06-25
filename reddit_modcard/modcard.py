from r2.controllers import add_controller
from r2.controllers.reddit_base import RedditController
from r2.lib.validator import VSrModerator, VAccountByName, VBoolean, validate
from pylons import c
from pages import ModCardPage

@add_controller
class ModCardController(RedditController):
    @validate(VSrModerator(),
              user=VAccountByName('user'))
    def GET_modcard(self, user):
        is_moderator = c.site.is_moderator(user)
        is_contributor = c.site.is_contributor(user)
        is_moderator_invited = c.site.get_moderator_invite(user)
        is_banned = c.site.is_banned(user)
        permissions = is_moderator.get_permissions() if is_moderator else None
        sr_link_karma = user.karma('link', c.site)
        sr_comment_karma = user.karma('comment', c.site)
        return ModCardPage(user,
                           permissions=permissions,
                           is_moderator=is_moderator,
                           is_moderator_invited=is_moderator_invited,
                           is_contributor=is_contributor,
                           is_banned=is_banned,
                           sr_link_karma=sr_link_karma,
                           sr_comment_karma=sr_comment_karma).render()
