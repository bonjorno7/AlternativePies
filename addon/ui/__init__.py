import bpy
from . import pies


classes = (
    pies.ShadingPie,
    pies.ViewPie,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
