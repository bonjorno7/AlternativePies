import bpy
from .. import utils


class SelectHierarchy(bpy.types.Operator):
    bl_idname = 'altpies.select_hierarchy'
    bl_label = 'Select Hierarchy'
    bl_description = 'Select all parents and children of the clicked object'
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D' and context.mode == 'OBJECT'


    def invoke(self, context, event):
        if not event.shift and not event.ctrl:
            bpy.ops.object.select_all(action='DESELECT')

        before = set(context.selected_objects)
        bpy.ops.view3d.select('INVOKE_DEFAULT', extend=event.shift, deselect=event.ctrl)
        after = set(context.selected_objects)

        for object in (before - after):
            for child in utils.select.hierarchy(object):
                child.select_set(False)

        for object in (after - before):
            for child in utils.select.hierarchy(object):
                child.select_set(True)

        return {'FINISHED'}
