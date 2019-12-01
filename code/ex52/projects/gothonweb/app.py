from flask import Flask, session, redirect, url_for, request
from flask import render_template
from gothonweb import planisphere


app = Flask(__name__)

@app.route("/")
def index():
    # 初期値でセッションをセットアップする。
    session['room_name'] = planisphere.START
    return redirect(url_for("game"))

@app.route("/game", methods=['GET', 'POST'])
def game():
    room_name = session.get('room_name')

    if request.method == "GET":
        if room_name:
            room = planisphere.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            # このコードがあるのはなぜだろうか? これは必要だろうか?
            return render_template("you_died.html")
    else:
        action = request.form.get('action')

        if room_name and action:
            room = planisphere.load_room(room_name)
            next_room = room.go(action)

            if not next_room:
                session['room_name'] = planisphere.name_room(room)
            else:
                session['room_name'] = planisphere.name_room(next_room)

        return redirect(url_for("game"))


# 注意: インターネット上に公開する場合は、この値を必ず変更すること!!
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
