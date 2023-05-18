from app import bigapp, db
from app.models.example_mixin import ExampleMixin
from flask_bigapp import Auth
from .. import bp


@bp.route("/database-creation", methods=["GET"])
def database_creation_test():
    db.drop_all()
    db.create_all()
    return "Database created."


@bp.route("/database-population", methods=["GET"])
def database_population_test():
    db.drop_all()
    db.create_all()

    m_example_user = bigapp.model("ExampleUser")
    m_example_user_bind = bigapp.model("ExampleUserBind")
    m_example_table = bigapp.model("ExampleTable")

    if not m_example_user.get_by_id(1):
        salt = Auth.generate_salt()
        gen_password = Auth.generate_password("animals")
        password = Auth.sha_password(gen_password, salt)

        new_example_user = m_example_user(
            username="David",
            password=password,
            salt=salt,
            private_key=Auth.generate_private_key(salt),
            disabled=False
        )
        db.session.add(new_example_user)
        new_example_user_bind = m_example_user_bind(
            username="David",
            password=password,
            salt=salt,
            private_key=Auth.generate_private_key(salt),
            disabled=False
        )
        db.session.add(new_example_user_bind)
        db.session.flush()
        new_example_user_rel = m_example_table(
            user_id=new_example_user.user_id,
            thing=gen_password
        )
        db.session.add(new_example_user_rel)
        db.session.flush()
        db.session.commit()

        user_in_example_table = bigapp.model("ExampleTable").get_by_user_id(new_example_user.user_id)

        if user_in_example_table:
            return (f"{new_example_user.username} created and {user_in_example_table.thing}"
                    f"in ExampleTable, and {new_example_user_bind.username} created in ExampleUserBind.")

    return "Failed Auto Test, User already exists."


@bp.route("/mixin-add", methods=["GET"])
def mixin_add_test():
    new_mixin = ExampleMixin.create({"thing": "MixinTest"})
    return f"{new_mixin.thing}"
