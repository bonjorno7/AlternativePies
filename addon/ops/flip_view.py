import bpy
import math
from .. import utils


class FlipView(bpy.types.Operator):
    bl_idname = 'altpies.flip_view'
    bl_label = 'Flip View'
    bl_description = 'Flip orthographic side views, otherwise rotate 180 degrees around the Z axis'
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'


    def execute(self, context):
        if context.region_data.is_orthographic_side_view:
            axis = utils.view.closest_axis(flip=True)
            bpy.ops.view3d.view_axis(type=axis)

        else:
            angle, axis = math.radians(180), 'ORBITRIGHT'
            bpy.ops.view3d.view_orbit(angle=angle, type=axis)

        return {'FINISHED'}
