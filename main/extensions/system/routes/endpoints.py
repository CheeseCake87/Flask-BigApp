from flask import current_app
from flask import render_template

from ....builtins.functions.security import login_required

from .. import bp
from .. import struc


@bp.route("/endpoints", methods=["GET"])
@login_required("auth", "account.login")
def endpoints():
    render = "renders/endpoints.html"
    structure = struc.name()
    extend = struc.extend("backend.html")
    footer = struc.include("footer.html")

    endpoints_dict = {}
    for rule in current_app.url_map.iter_rules():
        endpoints_dict[rule.endpoint] = rule.rule

    return render_template(
        render,
        structure=structure,
        extend=extend,
        footer=footer,
        endpoints=sorted(endpoints_dict.items())
    )
