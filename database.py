from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker)
from sqlalchemy.ext.declarative import declarative_base



engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for queryings
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import Tasks
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    first_task = Tasks(id=0, title = "Doctor Appointment", description="Have to go to see the doctor @ 9 a.m", done=False)
    db_session.add(first_task)
    db_session.commit()
