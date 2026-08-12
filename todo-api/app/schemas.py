from marshmallow import Schema, fields, validate 


class TaskSchema(Schema): 
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1, max=100), error_messages={"required": "O titulo e obrigatorio."})
    description = fields.Str(allow_none=True)
    done = fields.Bool(dump_default=False, load_default=False)

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
