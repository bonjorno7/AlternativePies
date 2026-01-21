import bpy


def hierarchy(object):
    '''Gather the entire hierarchy of this object.'''
    while object.parent:
        object = object.parent

    return [object] + object.children_recursive
