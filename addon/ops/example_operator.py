import bpy


class ExampleOperator(bpy.types.Operator):
    bl_idname = 'example.example_operator'
    bl_label = 'Example Operator'
    bl_description = 'Test test'
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'


    def execute(self, context):
        self.report({'INFO'}, 'Nothing to see here')
        return {'FINISHED'}
