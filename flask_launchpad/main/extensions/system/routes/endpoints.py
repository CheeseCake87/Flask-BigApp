from ....builtins.functions.security import login_required
from .. import bp
from .. import struc
from flask import current_app
from flask import render_template


@bp.route("/endpoints", methods=["GET"])
@login_required("auth", "account.login")
def endpoints():
    render = "renders/endpoints.html"
    structure = struc.name()
    extend = struc.extend("backend.html")
    footer = struc.include("footer.html")



    return render_template(
        render,
        structure=structure,
        extend=extend,
        footer=footer,
        endpoints=endpoints_dict
    )
