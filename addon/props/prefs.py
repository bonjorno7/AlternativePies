import bpy
import rna_keymap_ui
from .. import keymaps
from .. import utils


class AddonPrefs(bpy.types.AddonPreferences):
    bl_idname = utils.addon.module()


    def draw(self, context):
        layout = self.layout

        kc = bpy.context.window_manager.keyconfigs.addon
        km = keymaps.view_3d.keymap

        col = layout.column()
        col.context_pointer_set('keymap',  km)

        for kmi in keymaps.view_3d.items:
            rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)
