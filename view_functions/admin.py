from flask import Blueprint, render_template, redirect, url_for

admin_blp = Blueprint("admin", __name__)


@admin_blp.route('/account', methods=['GET', 'POST'])
def account():
    return render_template('account.html')


@admin_blp.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')


@admin_blp.route('/bonus_profit', methods=['GET', 'POST'])
def bonus_profit():
    return render_template('bonus_profit.html')


@admin_blp.route('/net_profit', methods=['GET', 'POST'])
def net_profit():
    return render_template('net_profit.html')
