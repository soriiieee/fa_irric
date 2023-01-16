from flask import Blueprint,request,render_template, redirect, url_for
from flask_login import login_user, login_required,logout_user

from sample1.forms import LoginForm , RegisterForm #作成した申込formの形をimportしてくる
from sample1.models import User #作成した自作のモデルクラスのひな形


### konomoduleを読み出す場合、appと指定して読み出す必要がある
bp = Blueprint("app" , __name__, url_prefix  = "")

@bp.route("/")
def home(): #loginする前に表示される画面
    return render_template("home.jinja")

#ログインしていないと実行されない
@bp.route("/welcome")
@login_required
def welcome():
    return render_template("welcome.jinja")

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("app.login"))

##################
@bp.route("/login",methods= ["GET" ,"POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.select_by_email(form.email.data) #emailから取得してくる
        
        if user and user.validate_password(form.password.data):
            login_user(user,remember=True) #sessionにログインユーザを保存する。(ログインした状態を保持する/ブラウザが切れてもセッションが維持される)
            next = request.args.get("next") #次のURL
            if not next:
                next = url_for("app.welcome") #ログイン直後の画面に移動させる(ulr_forにURL記載されているので保存する)
            return redirect(next)
    ##get-method(画面に来た場合は、ログイン画面に遷移させる)
    return render_template("login.jinja" , form=form)

@bp.route("/register" , methods = ["GET" ,"POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        user = User(
            email = form.email.data,
            username = form.username.data,
            password = form.password.data
        )
        user.add_user()
        return redirect(url_for("app.login"))
    return render_template("register.jinja" , form=form)

@bp.route("/user")
@login_required
def user():
     return render_template("user.jinja")


            
            
