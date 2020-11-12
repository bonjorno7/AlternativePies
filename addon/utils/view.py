import bpy
import mathutils


def closest_axis(flip: bool = False):
    '''Find the closest axis to the current view.'''
    quat = bpy.context.region_data.view_rotation
    axis = quat @ mathutils.Vector((0, 0, 1))

    array = [abs(x) for x in axis.xyz]
    index = array.index(max(array))
    value = axis.xyz[index]

    if flip:
        value *= -1

    if value > 0:
        axes = ['RIGHT', 'BACK', 'TOP']
    else:
        axes = ['LEFT', 'FRONT', 'BOTTOM']

    return axes[index]
