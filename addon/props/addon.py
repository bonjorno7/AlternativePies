import bpy
from .. import utils


class AddonProps(bpy.types.PropertyGroup):
    @property
    def module(self):
        return utils.addon.module()

    @property
    def prefs(self):
        return utils.addon.prefs()
