# api_login_check

```
Menu = flask_imp.security/api_login_check
Title = api_login_check
```


```python
from flask_imp.security import api_login_check
```

```python
api_login_check(
    session_key: str,
    values_allowed: t.Union[t.List[t.Union[str, int, bool]], str, int, bool],
    fail_json: t.Optional[t.Dict[str, t.Any]] = None,
    fail_status: int = 401,
)
```

`@api_login_check(...)`

**Marked for deprecation**

Use `@api_checkpoint(...)` instead.

---

A decorator that is used to secure API routes that return JSON responses.

`session_key` The session key to check for.

`values_allowed` A list of or singular value(s) that the session key must contain.

`fail_json` JSON that is returned on failure. `{"error": "You are not logged in."}` by default.

`fail_status` The status code to return on failure. `401` by default.

*Example:*

```python
@bp.route("/api/resource", methods=["GET"])
@api_login_check('logged_in', True)
def api_page():
    ...
```

**Example of defined fail_json:**

```python
@bp.route("/api/resource", methods=["GET"])
@api_login_check('logged_in', True, fail_json={"failed": "You need to be logged in."})
def api_page():
    ...
```

