import bpy


def module() -> str:
    '''The top level module for this addon.'''
    return __name__.partition('.')[0]


def prefs() -> bpy.types.AddonPreferences:
    '''The preferences for this addon.'''
    return bpy.context.preferences.addons[module()].preferences
