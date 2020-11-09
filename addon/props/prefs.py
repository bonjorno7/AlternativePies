import bpy
from .. import utils


class AddonPrefs(bpy.types.AddonPreferences):
    bl_idname = utils.addon.module()


    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.label(text='This area is under construction.')
