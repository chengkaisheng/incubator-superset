import logging

from flask_appbuilder.const import LOGMSG_WAR_SEC_LOGIN_FAILED

from superset.security.custom_view import MyAuthRemoteView
from superset.security.manager import SupersetSecurityManager

logger = logging.getLogger(__name__)


class MySecurityManager(SupersetSecurityManager):
    logger.info('use custom remote auth')
    authremoteuserview = MyAuthRemoteView

    def auth_user_remote_user_with_password(self, username, password):
        """
            Override from auth_user_remote_user()
            simply add a param password

            :param username: user's username for remote auth
            :param password: user's password for remote auth
            :type self: User model
        """
        user = self.find_user(username=username)

        # User does not exist, create one if auto user registration.
        if user is None and self.auth_user_registration:
            user = self.add_user(
                # All we have is REMOTE_USER, so we set
                # the other fields to blank.
                username=username,
                first_name=username,
                last_name="-",
                email=username + "@email.notfound",
                role=self.find_role(self.auth_user_registration_role),
                password=password
            )

        # If user does not exist on the DB and not auto user registration,
        # or user is inactive, go away.
        elif user is None or (not user.is_active):
            logger.info(LOGMSG_WAR_SEC_LOGIN_FAILED.format(username))
            return None

        self.update_user_auth_stat(user)
        return user
