from flask import render_template, session

from flask_imp.security import login_check, permission_check, pass_function_check
from .. import bp


@bp.route("/login/bool", methods=["GET"])
def login_bool():
    session["logged_in"] = True
    return render_template(bp.tmpl("security.html"), logged_in=True)


@bp.route("/login/str", methods=["GET"])
def login_str():
    session["logged_in"] = "li"
    return render_template(bp.tmpl("security.html"), logged_in=True)


@bp.route("/login/int", methods=["GET"])
def login_int():
    session["logged_in"] = 1
    return render_template(bp.tmpl("security.html"), logged_in=True)


@bp.route("/logout", methods=["GET"])
def logout():
    if session.get("logged_in"):
        del session["logged_in"]
    return render_template(bp.tmpl("security.html"), logged_in=False)


@bp.route("/set-permission/list", methods=["GET"])
def set_permissions_list():
    session["permissions"] = ["admin"]
    return render_template(bp.tmpl("security.html"), permissions=["admin"])


@bp.route("/set-permission/value", methods=["GET"])
def set_permissions_value():
    session["permissions"] = "admin"
    return render_template(bp.tmpl("security.html"), permission="admin")


@bp.route("/already-logged-in/bool/with-flash", methods=["GET"])
@login_check("logged_in", True, pass_endpoint="tests.already_logged_in", message="Already logged in")
def already_logged_in_bool():
    return render_template(bp.tmpl("security.html"), logged_in_on=session.get("logged_in"))


@bp.route("/must-be-logged-in/bool", methods=["GET"])
@login_check("logged_in", True, "tests.login_failed")
def must_be_logged_in_bool():
    return render_template(bp.tmpl("security.html"), logged_in_on=True)


@bp.route("/must-be-logged-in/bool/with-flash", methods=["GET"])
@login_check("logged_in", True, "tests.login_failed", message="Login needed")
def must_be_logged_in_bool_with_flash():
    return render_template(bp.tmpl("security.html"), logged_in_on=True)


@bp.route("/must-be-logged-in/str", methods=["GET"])
@login_check("logged_in", "li", "tests.login_failed")
def must_be_logged_in_str():
    return render_template(bp.tmpl("security.html"), logged_in_on="li")


@bp.route("/must-be-logged-in/int", methods=["GET"])
@login_check("logged_in", 1, "tests.login_failed")
def must_be_logged_in_int():
    return render_template(bp.tmpl("security.html"), logged_in_on=1)


@bp.route("/must-be-logged-in/multi", methods=["GET"])
@login_check("logged_in", [1, "li", True], "tests.login_failed")
def must_be_logged_in_multi():
    return render_template(bp.tmpl("security.html"), logged_in_on=session.get("logged_in"))


@bp.route("/must-have-permissions/std", methods=["GET"])
@permission_check("permissions", ["admin", "manager"], "tests.permission_failed")
def permission_check_std():
    return render_template(bp.tmpl("security.html"))


@bp.route("/must-have-permissions/adv", methods=["GET"])
@permission_check("permissions", ["super-admin"], "tests.permission_failed")
def permission_check_adv():
    return render_template(bp.tmpl("security.html"))


def check_if_number(number=1):
    try:
        int(number)
        return True
    except ValueError:
        return False


def blank_func(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


@bp.route("/pass-func-check", methods=["GET"])
@pass_function_check(check_if_number, "tests.permission_failed", fail_on_missing_function_kwargs=True)
def pass_function_check_std():
    return render_template(bp.tmpl("security.html"))


@bp.route("/pass-func-check-with-url-var/<number>", methods=["GET"])
@pass_function_check(check_if_number, "tests.permission_failed")
def pass_function_check_with_url_value(number):
    return render_template(bp.tmpl("security.html"))


@bp.route("/login-failed", methods=["GET"])
def login_failed():
    return render_template(bp.tmpl("login_failed.html"))


@bp.route("/already-logged-in", methods=["GET"])
def already_logged_in():
    return render_template(bp.tmpl("already_logged_in.html"))


@bp.route("/permission-failed", methods=["GET"])
def permission_failed():
    return "Permission failed"
