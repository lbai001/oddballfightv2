from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import MyModel
from ..models import Character


@view_config(route_name='home', renderer='../templates/home.mako')
def my_view(request):
    try:
        query = request.dbsession.query(MyModel)
        one = query.filter(MyModel.test == 2).first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': one, 'project': 'hi'}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_obf_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""


@view_config(route_name='choose_character', renderer='../templates/me.mako')
def choose_character(request):
    characters = []
    for instances in request.dbsession.query(Character):
        characters.append(instances)
        instances.hi()
    if request.params.get('user'):
        user = request.params.get('user')
        query = request.dbsession.query(Character)
        user_stat = query.filter(Character.id == user).first()
        return {'characters': characters, 'user': user_stat}
    return {'characters': characters}
