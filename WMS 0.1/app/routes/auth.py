from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app.models.models import User
from app import db

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:  # 실제 구현시에는 비밀번호 해싱 필요
            login_user(user)
            return redirect(url_for('main.index'))
        flash('잘못된 로그인 정보입니다.')
    return render_template('auth/login.html') 