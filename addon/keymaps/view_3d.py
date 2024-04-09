import bpy


keymap = None
items = []


def register(keyconfig: bpy.types.KeyConfig):
    global keymap

    if keymap is None:
        keymap = keyconfig.keymaps.new(name="3D View", space_type="VIEW_3D")

        item = keymap.keymap_items.new('wm.call_menu_pie', 'Z', 'PRESS')
        item.properties.name = 'ALTPIES_MT_ShadingPie'
        items.append(item)

        item = keymap.keymap_items.new('wm.call_menu_pie', 'ACCENT_GRAVE', 'PRESS')
        item.properties.name = 'ALTPIES_MT_ViewPie'
        items.append(item)


def unregister(keyconfig: bpy.types.KeyConfig):
    global keymap

    if keymap is not None:
        keyconfig.keymaps.remove(keymap)

        keymap = None
        items.clear()
