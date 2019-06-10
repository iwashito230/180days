from bottle import route, run
from bottle import jinja2_template as template
from bottle import static_file


@route('/css/<filename>')
def css_dir(filename):
    return static_file(filename, root='./static/css')


@route('/css/nivo-lightbox/<filename>')
def css_nivo_dir(filename):
    return static_file(filename, root='./static/css/nivo-lightbox')


@route('/js/<filename>')
def js_dir(filename):
    return static_file(filename, root='./static/js')


@route('/img/<filename:path>')
def img_dir(filename):
    return static_file(filename, root='./static/img')


@route('/fonts/<filename>')
def fonr_dir(filename):
    return static_file(filename, root='./static/fonts')


@route('/')
def top():
    return template('index')


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
