import bpy


class SnapView(bpy.types.Operator):
    bl_idname = 'altpies.snap_view'
    bl_label = 'Snap View'
    bl_description = 'Snap view to the closest axis'
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'


    def execute(self, context):
        self.report({'INFO'}, 'TODO: Actually implement this feature')
        return {'FINISHED'}
