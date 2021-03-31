from flask import Flask, render_template, url_for, request, redirect, session, jsonify
from data import queries
from flask_session import Session


app = Flask('codecool_series')
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)


@app.route('/')
def index():
    shows = queries.get_shows()
    if session["logged_in"] == True:
        return render_template('index.html', shows=shows)
    else:
        return render_template("login.html", message="Nem vagy bejelentkezve!")


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


@app.route('/registration', methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        queries.save_users(request.form["e-mail"], request.form["password"])
        return render_template('succes_registration.html')
    else:
        return render_template('registration.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        users = queries.list_users(
            request.form["e-mail"], request.form["password"])
        print(users)
        if len(users) != 0:
            session["logged_in"] = True
            return redirect("/")
        else:
            return render_template("login.html", message="Sikertelen bejelentkezés!")

    return render_template('login.html')


@app.route('/test', methods=["GET"])
def test():
    return session.get("logged_in", "False")


@app.route('/tv-show/<string:id>')
def film_desciption(id):
    show_detail = queries.get_show(id)
    print(show_detail)
    return render_template("show_details.html", show_detail=show_detail[0])


@app.route('/top')
def rated_shows():
    return render_template("top_rating.html")


@app.route('/api/top/<int:page>')
def api(page):
    page_number = page
    if page == None:
        page = 1
    top_shows = queries.top_shows(page_number)
    return jsonify(top_shows)


if __name__ == '__main__':
    main()
