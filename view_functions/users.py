from flask import Blueprint, render_template

user = Blueprint("users", __name__)


@user.route('/')
def index():
    return render_template('index.html')


@user.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@user.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@user.route('/bitcoin_chart', methods=['GET', 'POST'])
def bitcoin_chart():
    return render_template('bitcoin_chart.html')


@user.route('/user', methods=['GET', 'POST'])
def user_dash():
    return render_template('user.html')


@user.route('/blog', methods=['GET', 'POST'])
def blog():
    return render_template('blog.html')


@user.route('/faq', methods=['GET', 'POST'])
def faq():
    return render_template('faq.html')


@user.route('/investment_plan', methods=['GET', 'POST'])
def investment_plan():
    return render_template('investment_plan.html')


@user.route('/server_error_page', methods=['GET', 'POST'])
def server_error_page():
    return render_template('server_error_page.html')


@user.route('/service', methods=['GET', 'POST'])
def service():
    return render_template('service.html')


@user.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    return render_template('sign_up.html')


@user.route('/team', methods=['GET', 'POST'])
def team():
    return render_template('team.html')


@user.route('/terms_of_service', methods=['GET', 'POST'])
def terms_of_service():
    return render_template('terms_of_service.html')


@user.route('/error_404', methods=['GET', 'POST'])
def error_404():
    return render_template('error_404.html')


@user.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')


@user.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    return render_template('reset_password.html')
