import logging

from flask import request, g, redirect, flash
from flask_appbuilder._compat import as_unicode
from flask_appbuilder.security.views import AuthRemoteUserView
from flask_appbuilder.views import expose
from flask_login import login_user

logger = logging.getLogger(__name__)


class MyAuthRemoteView(AuthRemoteUserView):
    @expose('/login')
    def login(self):
        logger.info('use custom remote auth')

        username = request.args.get('username')
        password = request.args.get('password')
        if g.user is not None and g.user.is_authenticated:
            return redirect(self.appbuilder.get_url_for_index)
        if username:
            user = self.appbuilder.sm.auth_user_remote_user_with_password(
                username=username,
                password=password
            )
            if user:
                login_user(user)
            else:
                flash(as_unicode(self.invalid_login_message), 'warning')
        else:
            flash(as_unicode(self.invalid_login_message), 'warning')
        return redirect(self.appbuilder.get_url_for_index)
