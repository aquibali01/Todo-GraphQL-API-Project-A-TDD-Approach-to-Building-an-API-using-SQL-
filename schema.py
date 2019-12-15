import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import Tasks as TasksModel
import utils
from database import db_session

class Tasks(SQLAlchemyObjectType):
    class Meta:
        model = TasksModel
        interfaces = (relay.Node, )

# class CreateTaskInput(graphene.InputObjectType, Tasks):
#     pass

# class CreateTask(graphene.Mutation):
#     task = graphene.Field(lambda:Tasks, description="Tasks created by this mutation")

#     class Arguments:
#         input = CreateTaskInput(required=True)

#     def mutate(self,info, input):
#         data = utils.input_to_dictionary(input)

#         task = TasksModel(**data)
#         db_session.add(task)
#         db_session.commit()

#         return CreateTask(task=task)

# class Mutation(graphene.ObjectType):
#     createTask = CreateTask.Field()

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_tasks = SQLAlchemyConnectionField(Tasks)

    # def resolve_tasks(self, info):
    #     return list(TasksModel.objects.all())

schema = graphene.Schema(query=Query) # mutation=Mutation )
