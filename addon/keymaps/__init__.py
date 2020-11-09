import bpy
from . import view_3d


modules = (
    view_3d,
)


def register():
    keyconfig = bpy.context.window_manager.keyconfigs.addon

    for module in modules:
        module.register(keyconfig)


def unregister():
    keyconfig = bpy.context.window_manager.keyconfigs.addon

    for module in modules:
        keyconfig.keymaps.remove(module.keymap)
