"""Web Routes."""

from masonite.routes import Get, Post, RouteGroup

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),
    Get('/projects', 'ProjectController@index').name('projects.index'),
    Get('/projects/@id', 'ProjectController@show').name('projects.show').middleware('helloworld'),

    RouteGroup([
        Get('/', 'PostController@index').name('index'),
        Get('/@id', 'PostController@show').name('show'),
        Get('/create', 'PostController@create').name('create'),
        Post('/store', 'PostController@store').name('store')
    ], prefix='/blog', name='blog.')
]

ROUTES = ROUTES + [
    Get().route('/login', 'LoginController@show').name('login'),
    Get().route('/logout', 'LoginController@logout').name('logout'),
    Post().route('/login', 'LoginController@store'),
    Get().route('/register', 'RegisterController@show').name('register'),
    Post().route('/register', 'RegisterController@store'),
    Get().route('/home', 'HomeController@show').name('home'),
    Get().route('/email/verify', 'ConfirmController@verify_show').name('verify'),
    Get().route('/email/verify/send', 'ConfirmController@send_verify_email'),
    Get().route('/email/verify/@id:signed', 'ConfirmController@confirm_email'),
    Get().route('/password', 'PasswordController@forget').name('forgot.password'),
    Post().route('/password', 'PasswordController@send'),
    Get().route('/password/@token/reset', 'PasswordController@reset').name('password.reset'),
    Post().route('/password/@token/reset', 'PasswordController@update'),
]
