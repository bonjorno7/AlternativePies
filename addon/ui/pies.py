import bpy


class ShadingPie(bpy.types.Menu):
    bl_idname = 'ALTPIES_MT_ShadingPie'
    bl_label = 'Shading'

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        view = context.space_data

        pie.prop_enum(view.shading, 'type', value='WIREFRAME')
        pie.prop_enum(view.shading, 'type', value='SOLID')

        if context.pose_object:
            pie.prop(view.overlay, 'show_xray_bone', icon='XRAY')

        else:
            if context.mode == 'EDIT_MESH' or view.shading.type in {'SOLID', 'WIREFRAME'}:
                sub = pie
            else:
                sub = pie.row()
                sub.active = False

            prop = 'show_xray_wireframe' if view.shading.type == 'WIREFRAME' else 'show_xray'
            sub.prop(view.shading, prop, text='Toggle X-Ray', icon='XRAY',)

        pie.prop(view.overlay, 'show_overlays', text='Toggle Overlays', icon='OVERLAY')

        pie.prop_enum(view.shading, 'type', value='MATERIAL')
        pie.prop_enum(view.shading, 'type', value='RENDERED')

        pie.prop(view.overlay, 'show_wireframes', text='Toggle Wireframes', icon='MOD_WIREFRAME')
        pie.prop(view.overlay, 'show_face_orientation', text='Toggle Face Orientation', icon='ORIENTATION_NORMAL')
