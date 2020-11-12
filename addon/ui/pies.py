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

        elif context.mode == 'EDIT_MESH' or view.shading.type in {'SOLID', 'WIREFRAME'}:
            prop = 'show_xray_wireframe' if view.shading.type == 'WIREFRAME' else 'show_xray'
            pie.prop(view.shading, prop, text='Toggle X-Ray', icon='XRAY')

        else:
            row = pie.row()
            row.emboss = 'RADIAL_MENU'
            row.scale_x = 1.2
            row.scale_y = 1.5
            row.enabled = False
            row.prop(view.shading, 'show_xray', text='Toggle X-Ray', icon='XRAY')

        pie.prop(view.overlay, 'show_overlays', text='Toggle Overlays', icon='OVERLAY')

        pie.prop_enum(view.shading, 'type', value='MATERIAL')
        pie.prop_enum(view.shading, 'type', value='RENDERED')

        pie.prop(view.overlay, 'show_wireframes', text='Toggle Wireframes', icon='MOD_WIREFRAME')
        pie.prop(view.overlay, 'show_face_orientation', text='Toggle Face Orientation', icon='ORIENTATION_NORMAL')


class ViewPie(bpy.types.Menu):
    bl_idname = 'ALTPIES_MT_ViewPie'
    bl_label = 'View'

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        text = 'View Perspective' if context.region_data.view_perspective == 'ORTHO' else 'View Ortho'
        icon = 'VIEW_PERSPECTIVE' if context.region_data.view_perspective == 'ORTHO' else 'VIEW_ORTHO'
        pie.operator('view3d.view_persportho', text=text, icon=icon)
        pie.operator('altpies.snap_view', text='Snap View', icon='ORIENTATION_VIEW')

        pie.operator('view3d.view_all', text='View All', icon='ZOOM_ALL')
        pie.operator('view3d.localview', text='Local View', icon='ORIENTATION_LOCAL')

        op = pie.operator('wm.call_panel', text='NDOF Settings', icon='PREFERENCES')
        op.name = 'USERPREF_PT_ndof_settings'
        op = pie.operator('view3d.view_orbit', text='View Other Side', icon='FILE_REFRESH')
        op.angle, op.type = 3.14159, 'ORBITRIGHT'

        pie.operator('view3d.view_camera', text='View Camera', icon='CAMERA_DATA')
        pie.operator('view3d.view_selected', text='View Selected', icon='ZOOM_SELECTED')
