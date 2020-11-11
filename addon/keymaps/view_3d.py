import bpy


keymap = None


def register(keyconfig: bpy.types.KeyConfig):
    global keymap
    keymap = keyconfig.keymaps.new(name="3D View", space_type="VIEW_3D")
