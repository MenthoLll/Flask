from flask import Flask


app: Flask = Flask(__name__)

@app.route("/home")
def home_page() -> None:
    return f"""
    <a href="/end">END</a>
    """


@app.route("/end")
def end_point() -> None:
    return f"""
    Я <b>знал</b> что ты придёшь !
    """


if __name__ == '__main__':
    app.run(
        port=8080,
        debug=True
    )