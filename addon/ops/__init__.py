import bpy
from . import snap_view
from . import flip_view
from . import select_hierarchy


classes = (
    snap_view.SnapView,
    flip_view.FlipView,
    select_hierarchy.SelectHierarchy,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
