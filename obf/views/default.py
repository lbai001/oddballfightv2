from pyramid.response import Response
from pyramid.view import view_config
import json
from sqlalchemy.exc import DBAPIError

from ..models import MyModel, Character, Skill, Game


@view_config(route_name='home', renderer='../templates/home.mako')
def my_view(request):
    try:
        query = request.dbsession.query(Character)
        one = query.filter(Character.id == 4).first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': 1, 'project': 'hi'}


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


@view_config(route_name='test', renderer='json')
def test(request):
    skills = request.dbsession.query(Skill).all()
    return skills


@view_config(route_name='choose_character', renderer='../templates/me.mako')
def choose_character(request):
    characters = []
    for instances in request.dbsession.query(Character):
        characters.append(instances)

    # show selected player stats
    # if request.params.get('user'):
    #     user = request.params.get('user')
    #     query = request.dbsession.query(Character)
    #     user_stat = query.filter(Character.id == user).first()
    #     print (user_stat.skills)
    #     skill_query = request.dbsession.query(Skill)
    #     user_skill = skill_query.filter(Skill.player_id == user).all()
    #     return {'characters': characters, 'user': user_stat, 'skill': user_skill, 'opponents': possible_opponents, 'opponent': request.params.get('opponent')}

    return {'characters': characters, 'num': 0}


@view_config(route_name='stat', renderer='../templates/stat.mako')
def show_stat(request):
    user_id = request.params.get('user')
    query = request.dbsession.query(Character)
    user = query.filter(Character.id == user_id).first()
    print(user.skills)
    game_player = Game(player=user, opponent=None, end_fight=False)
    request.dbsession.add(game_player)
    return {"user": user}
