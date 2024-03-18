from functools import wraps
from flask import session, redirect, url_for

def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        current_user = session.get('user')
        if current_user is None:
            return redirect(url_for('login.login'))
        return view(*args, **kwargs)
    return wrapped_view

def login_required_admin(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        current_user = session.get('user')
        if current_user is None:
            return redirect(url_for('login.login'))
        elif not current_user['isAdmin']:
            return redirect(url_for('user.index'))
        return view(*args, **kwargs)
    return wrapped_view