import bpy


class RefreshLibraries(bpy.types.Operator):
    bl_idname = 'altpies.refresh_libraries'
    bl_label = 'Refresh Libraries'
    bl_description = 'Refresh all linked libraries'
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'


    def execute(self, context):
        for library in bpy.data.libraries:
            library.reload()

        return {'FINISHED'}
