from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user
import flask_restless
import os
from ..models import *

app = Flask(__name__)

def setup_app():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SECRET_KEY'] = 'you dont know this'
    app.config['SQLALCHEMY_DATABASE_URI'] = get_sqlalchemy_uri()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


setup_app()


db = SQLAlchemy(app, model_class=Base)
login = LoginManager(app)

@login.user_loader
def load_user(id):
    return db.session.query(User).get(int(id))

@app.context_processor
def inject_user():
    return dict(user=current_user)


# @app.before_first_request
# def init_app():
#     # set up admin stuff
#     admin = Admin(app, name='Admin')
#     admin.add_view(FigureView(Figure, db.session, category='Pieces'))
#     admin.add_view(WargearView(Wargear, db.session, category='Pieces'))
#     admin.add_view(ArmybuilderModelView(Keyword, db.session, category='Metadata'))
#     admin.add_view(ArmybuilderModelView(Ability, db.session, category='Rules'))
#     admin.add_view(ArmybuilderModelView(Specialization, db.session, category='Rules'))
#     admin.add_view(TacticView(Tactic, db.session, category='Rules'))
#     admin.add_view(RosterView(Roster, db.session, category='Roster'))
#     admin.add_view(RosterEntryView(RosterEntry, db.session, category='Roster'))
#     admin.add_view(ArmybuilderModelView(Faction, db.session, category='Metadata'))
#     admin.add_view(UserView(User, db.session, category='User'))
#     admin.add_view(ArmybuilderModelView(Role, db.session, category='User'))
#     admin.add_view(WargearProfileView(WargearProfile, db.session, category='Pieces'))
#     admin.add_view(ArmybuilderModelView(FigureProfile, db.session, category='Pieces'))

#     manager = flask_restless.APIManager(app, session=db.session)
#     manager.create_api(Roster, include_methods=['points'], methods=['GET', 'POST', 'PUT', 'DELETE'])
#     manager.create_api(RosterEntry, allow_delete_many=True, include_methods=['points'], methods=['GET', 'POST', 'PUT', 'DELETE'])
#     manager.create_api(Specialization, results_per_page=-1, methods=['GET', 'POST', 'PUT', 'DELETE'])
#     manager.create_api(Wargear, results_per_page=-1,  methods=['GET', 'POST', 'PUT', 'DELETE'])
#     manager.create_api(Figure, include_methods=['displayName'], results_per_page=-1, methods=['GET', 'POST', 'PUT', 'DELETE'])
#     manager.create_api(FigureProfile, methods=['GET', 'POST', 'PUT', 'DELETE'], results_per_page=-1)
#     manager.create_api(Keyword, methods=['GET', 'POST', 'PUT', 'DELETE'], results_per_page=-1)
#     manager.create_api(Faction, methods=['GET', 'POST', 'PUT', 'DELETE'], results_per_page=-1)
#     manager.create_api(Tactic, methods=['GET', 'POST', 'PUT', 'DELETE'], results_per_page=-1)
#     manager.create_api(Killteam, methods=['GET', 'POST', 'PUT', 'DELETE'], results_per_page=-1)


from . import views, api