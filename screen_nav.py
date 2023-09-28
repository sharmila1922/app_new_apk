screen_helper = """
#: import get_color_from_hex kivy.utils.get_color_from_hex

ScreenManager:
    id: sm
    TopPage:
        MDFloatLayout:
            md_bg_color: 43/255, 135/255, 168/255, 1
            Image:
                source: "static/myfiles/1.png"
                size_hint: .24,.24
                pos_hint: {"center_x":.5, "center_y":.55}
                canvas.before:
                    Color:
                        rgb: 1,1,1,1
        MDLabel:
            text: "SNOW REMOVAL"
            pos_hint: {"center_x":.7, "center_y":.4}
            haling: "center"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
            font_size: "38sp"
            font_name: "Comic"
        MDRoundFlatButton:
            text: "HOME"
            pos_hint: {"center_x":.5, "center_y":.3}
            font_size: 20
            md_bg_color: 0, 0, 0, 1
            on_press: app.root.current='menu'
    MenuScreen:
        MDTopAppBar:
            pos_hint: {"top": 1}
            title: "Snow Removal App"
            elevation: 8
            md_bg_color: 43/255, 135/255, 168/255, 1
    CustomerRegistration:
        id: customerreg
        MDTopAppBar:
            pos_hint: {"top": 1}
            title: "Snow Removal App"
            icon_left: "arrow"
            elevation: 8
            md_bg_color: 43/255, 135/255, 168/255, 1
    ServiceProviderReg:
        MDTopAppBar:
            pos_hint: {"top": 1}
            title: "Snow Removal App"
            icon_left: "arrow"
            elevation: 8
            md_bg_color: 43/255, 135/255, 168/255, 1
    AdminHome:
        MDTopAppBar:
            pos_hint: {"top": 1}
            title: "Snow Removal App"
            icon_left: "arrow"
            elevation: 8
            md_bg_color: 43/255, 135/255, 168/255, 1
        MDRoundFlatButton:
            text: "Admin Home"
            pos_hint: {"center_x":.5, "center_y":.3}
            font_size: 20
            md_bg_color: 0, 0, 0, 1
            on_press: app.root.current='adminmenu'
    AdminScreen:
        MDTopAppBar:
            pos_hint: {"top": 1}
            title: "Snow Removal App"
            icon_left: "arrow"
            elevation: 8
            md_bg_color: 43/255, 135/255, 168/255, 1
    ViewLocations:
        MDTopAppBar:
            pos_hint: {"top": 1}
            title: "Snow Removal App"
            icon_left: "arrow"
            elevation: 8
            md_bg_color: 43/255, 135/255, 168/255, 1
    ViewCategory:
        MDTopAppBar:
            pos_hint: {"top": 1}
            title: "Snow Removal App"
            icon_left: "arrow"
            elevation: 8
            md_bg_color: 43/255, 135/255, 168/255, 1
    

<MenuScreen>
    name: 'menu'
    admin_email : admin_email
    admin_password : admin_password
    MDBottomNavigation:
        md_bg_color: 43/255, 135/255, 168/255, 1
        MDBottomNavigationItem:
            name: "screen1"
            text: "Home"
            color:  1, 0, 0, 0.9
            font_name: "Comic"
            font_size: 20
            MDLabel:
                text: "Welcome to Snow Removal App"
                font_name: "Comic"
                font_size: 40
                halign: "center"
        MDBottomNavigationItem:
            name: "screen2"
            text: "Admin"
            font_name: "Comic"
            font_size: 20
            MDCard:
                size_hint: None,None
                size: 450,550
                pos_hint: {"center_x":.5,"center_y":.5}
                elevation: 5
                md_bg_color: [120, 120, 120]
                padding: 20
                spacing: 30
                orientation: "vertical"
                MDLabel:
                    text: "ADMIN LOGIN"
                    color:  0, 0, 0, 0.9
                    font_name: "Comic"
                    font_style: 'Button'
                    font_size: 40
                    halign: "center"
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding_y: 15
                MDTextField:
                    id: admin_email
                    mode: "round"
                    hint_text: "Email"
                    multiline: False
                    font_name: "Comic"
                    icon_right: "email"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                MDTextField:
                    id : admin_password
                    mode: "round"
                    hint_text: "Password"
                    font_name: "Comic"
                    icon_right: "eye-off"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                    password: True
                MDRoundFlatButton:
                    text: "LOGIN"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    on_press: root.admin_login()
                Widget:
                    size_hint_y: None
                    height: 30
        MDBottomNavigationItem:
            name: "screen3"
            text: "Service"
            font_name: "Comic"
            font_size: 20
            MDCard:
                size_hint: None,None
                size: 450,550
                pos_hint: {"center_x":.5,"center_y":.5}
                elevation: 5
                md_bg_color: [120, 120, 120]
                padding: 20
                spacing: 30
                orientation: "vertical"
                MDLabel:
                    text: "SERVICE PROVIDER LOGIN"
                    color:  0, 0, 0, 0.9
                    font_name: "Comic"
                    font_style: 'Button'
                    font_size: 40
                    halign: "center"
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding_y: 15
                MDTextField:
                    hint_text: "Email"
                    font_name: "Comic"
                    icon_right: "account"
                    mode: "round"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                    normal_color : [1,1,0,1]
                    on_text: self.text = self.text.replace(" ", "")
                MDTextField:
                    mode: "round"
                    hint_text: "Password"
                    font_name: "Comic"
                    icon_right: "eye-off"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                    password: True
                    on_text: self.text = self.text.replace(" ", "")
                MDRoundFlatButton:
                    text: "LOGIN"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                MDRectangleFlatButton:
                    text: "REGISTER HERE"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    on_press: root.manager.current='serviceproviderreg'
                Widget:
                    size_hint_y: None
                    height: 15
        MDBottomNavigationItem:
            name: "screen4"
            text: "Customer"
            font_name: "Comic"
            font_size: 20
            MDCard:
                size_hint: None,None
                size: 450,550
                pos_hint: {"center_x":.5,"center_y":.5}
                elevation: 5
                md_bg_color: [120, 120, 120]
                padding: 20
                spacing: 30
                orientation: "vertical"
                MDLabel:
                    text: "CUSTOMER LOGIN"
                    color:  0, 0, 0, 0.9
                    font_name: "Comic"
                    font_style: 'Button'
                    font_size: 40
                    halign: "center"
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding_y: 15
                MDTextField:
                    id: email
                    hint_text: "Email"
                    font_name: "Comic"
                    icon_right: "account"
                    mode: "round"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                    normal_color : [1,1,0,1]
                    on_text: self.text = self.text.replace(" ", "")
                MDTextField:
                    id: password
                    mode: "round"
                    hint_text: "Password"
                    font_name: "Comic"
                    icon_right: "eye-off"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                    password: True
                    on_text: self.text = self.text.replace(" ", "")
                MDRoundFlatButton:
                    text: "LOGIN"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    on_release: app.receive_data(email,password)
                MDRectangleFlatButton:
                    text: "REGISTER HERE"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    on_press: root.manager.current='customerreg'
                Widget:
                    size_hint_y: None
                    height: 15
<AdminHome>
    name: 'adminhome'
    MDLabel:
        text: "Welcome to Admin"
        font_name: "Comic"
        font_size: 40
        halign: "center"
    MDRoundFlatButton:
        text: "BACK"
        pos_hint: {"center_x":.5, "center_y":.2}
        font_size: 20
        md_bg_color: 0, 0, 0, 1
        on_press: app.root.current='menu'
        
<CustomerRegistration>
    name: 'customerreg'
    fname : fname
    email : email
    phone : phone
    password : password
    address : address
    longitude : longitude
    latitude : latitude
    MDCard:
        size_hint: None,None
        size: 500,550
        pos_hint: {"center_x":.5,"center_y":.5}
        elevation: 5
        md_bg_color: [120, 120, 120]
        padding: 10
        spacing: 10
        orientation: "vertical"
        MDLabel:
            text: "Customer Registration"
            color:  0, 0, 0, 0.9
            font_name: "Comic"
            font_style: 'Button'
            font_size: 25
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15
        TextInput:
            id: fname
            hint_text: "Name"
            multiline: False
            font_name: "Comic"
            icon_right: "account"
            mode: "round"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
            normal_color : [1,1,0,1]
        TextInput:
            id: email
            mode: "round"
            hint_text: "Email"
            multiline: False
            font_name: "Comic"
            icon_right: "email"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        TextInput:
            id: phone
            mode: "round"
            hint_text: "Phone"
            font_name: "Comic"
            icon_right: "phone"
            multiline: False
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        TextInput:
            id: password
            mode: "round"
            hint_text: "Password"
            multiline: False
            font_name: "Comic"
            icon_right: "eye-off"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
            password: True
            on_text: self.text = self.text.replace(" ", "")
        TextInput:
            id: address
            mode: "round"
            hint_text: "Address"
            multiline: False
            font_name: "Comic"
            icon_right: "address"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        TextInput:
            id: longitude
            mode: "round"
            hint_text: "Longitude"
            multiline: False
            font_name: "Comic"
            icon_right: "longitude"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        TextInput:
            id: latitude
            mode: "round"
            hint_text: "Latitude"
            multiline: False
            font_name: "Comic"
            icon_right: "latitude"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        MDRoundFlatButton:
            text: "REGISTER"
            pos_hint: {"center_x": .5}
            font_size: 20
            on_press: root.send_data()
        Widget:
            size_hint_y: None
            size_hint_y: None
            height: 15
        MDRoundFlatButton:
            text: "Go to Customer Login Page"
            pos_hint: {"center_x": .5}
            font_size: 20
            on_press: root.manager.current='menu'

<ServiceProviderReg>
    name: 'serviceproviderreg'
    sname : sname
    email : email
    password : password
    phone : phone
    address : address
    
    MDCard:
        size_hint: None,None
        size: 500,550
        pos_hint: {"center_x":.5,"center_y":.5}
        elevation: 5
        md_bg_color: [120, 120, 120]
        padding: 6
        spacing: 9
        orientation: "vertical"
        MDLabel:
            text: "Service Provider Registration"
            color:  0, 0, 0, 0.9
            font_name: "Comic"
            font_style: 'Button'
            font_size: 25
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15
        TextInput:
            id: sname
            hint_text: "Name"
            font_name: "Comic"
            icon_right: "account"
            mode: "round"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
            normal_color : [1,1,0,1]
        TextInput:
            id: email
            mode: "round"
            hint_text: "Email"
            font_name: "Comic"
            icon_right: "eye-off"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        TextInput:
            id: password
            mode: "round"
            hint_text: "Password"
            font_name: "Comic"
            icon_right: "eye-off"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
            password: True
            on_text: self.text = self.text.replace(" ", "")
        TextInput:
            id: phone
            mode: "round"
            hint_text: "Phone"
            font_name: "Comic"
            icon_right: "eye-off"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        TextInput:
            id: address
            mode: "round"
            hint_text: "Address"
            font_name: "Comic"
            icon_right: "eye-off"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        Widget:
            size_hint_y: None
            height: 19
        BoxLayout:
            size_hint: .85, None
            height: "30dp"
            pos_hint: {'center_x':.5, 'center_y':.3}
            spacing: "5dp"
            MDFlatButton:
                id: profile
                text: "Profile"
                size_hint_x: 2
                font_size: 20
                md_bg_color: 1, 0, 0, 1
                on_press : root.profile_button()
            Image:
                id : profile_img
            MDFlatButton
                id: licence
                text: "Licence"
                size_hint_x: 2
                font_size: 20
                md_bg_color: 1, 0, 0, 1
                on_press : root.licence_button()
            Image:
                id : licence_img
            MDFlatButton:
                id: idproof
                text: "ID Proof"
                size_hint_x: 2
                font_size: 20
                md_bg_color: 1, 0, 0, 1
                on_press : root.id_proof_button()
            Image:
                id : id_proof_img
        Widget:
            size_hint_y: None
            height: 19
        MDRoundFlatButton:
            text: "REGISTER"
            pos_hint: {"center_x": .5}
            spacing: 9
            font_size: 20
            on_press : root.register_data()
        Widget:
            size_hint_y: None
            height: 15
        MDRoundFlatButton:
            text: "Go to Service Provider Login Page"
            pos_hint: {"center_x": .5}
            font_size: 20
            on_press: root.manager.current='menu'

<AdminScreen>
    name: 'adminmenu'
    location_name : location_name
    longitude : longitude
    latitude : latitude
    category_name : category_name
    MDBottomNavigation:
        md_bg_color:43/255,135/255,168/255,1
        MDBottomNavigationItem:
            name: "screen6"
            text: "Locations"
            font_name: "Comic"
            font_size: 5
            MDCard:
                size_hint: None,None
                size: 450,460
                pos_hint: {"center_x":.5,"center_y":.5}
                elevation: 5
                md_bg_color: [120, 120, 120]
                padding: 9
                spacing: 5
                orientation: "vertical"
                MDTextField:
                    id : location_name
                    hint_text: "Location Name"
                    font_name: "Comic"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                    normal_color : [1,1,0,1]
                MDTextField:
                    id : longitude
                    hint_text: "Longitude"
                    font_name: "Comic"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                MDTextField:
                    id : latitude
                    hint_text: "Latitude"
                    font_name: "Comic"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                MDRoundFlatButton:
                    id: location_picture
                    text: "Select Location Picture"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    md_bg_color: 1, 0, 0, 1
                    on_press : root.location_button()
                Image:
                    id : location_picture
                MDRoundFlatButton:
                    text: "ADD LOCATION"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    on_press: root.add_location_data()
                MDRoundFlatButton:
                    text: "View Locations"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    on_press: root.view_locations()
        MDBottomNavigationItem:
            name: "screen8"
            text: "Providers"
            font_name: "Comic"
            font_size: 5
            cols: 9  # Set the number of columns
            ScrollView:
                GridLayout:
                    id: provider_table_layout
                    cols: 9
                    spacing: dp(10)  # Using density-independent pixels for spacing
                    padding: dp(10)  # Using density-independent pixels for padding
                    row_default_height: '10dp'
                    MDLabel:
                        text: 'Provider Name'
                    MDLabel:
                        text: 'Provider Email'
                    MDLabel:
                        text: 'Provider Phone'
                    MDLabel:
                        text: 'Provider Password'
                    MDLabel:
                        text: 'Provider Address'
                    MDLabel:
                        text: 'Profile'
                    MDLabel:
                        text: 'Licence'
                    MDLabel:
                        text: 'ID Proof'
                    MDLabel:
                        text: 'Status'
        MDBottomNavigationItem:
            name: "screen9"
            text: "Categories"
            font_name: "Comic"
            font_size: 5
            MDCard:
                size_hint: None,None
                size: 450,550
                pos_hint: {"center_x":.5,"center_y":.5}
                elevation: 5
                md_bg_color: [120, 120, 120]
                padding: 20
                spacing: 30
                orientation: "vertical"
                MDLabel:
                    text: "ADD CATEGORY"
                    color:  0, 0, 0, 0.9
                    font_name: "Comic"
                    font_style: 'Button'
                    font_size: 40
                    halign: "center"
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding_y: 15
                MDTextField:
                    id : category_name
                    hint_text: "Category Name"
                    font_name: "Comic"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                MDRoundFlatButton:
                    id: category_picture
                    text: "Select Category Picture"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    md_bg_color: 1, 0, 0, 1
                    on_press : root.category_button()
                Image:
                    id : category_image
                MDRoundFlatButton:
                    text: "ADD CATEGORY"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    on_press: root.add_category_data()
                MDRoundFlatButton:
                    text: "View Category"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    on_press: root.view_category()
                Widget:
                    size_hint_y: None
                    height: 30
        MDBottomNavigationItem:
            name: "screen11"
            text: "Home"
            font_name: "Comic"
            font_size: 5
            MDRoundFlatButton:
                text: "BACK TO HOME"
                pos_hint: {"center_x": .5}
                font_size: 20
                on_press: root.manager.current='menu'
<SelectableButton>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size
    on_press:
        root.var.populate_fields(self)

<ViewLocations>:
    name: 'viewlocations'
    cols: 4  # Set the number of columns
    ScrollView:
        GridLayout:
            id: location_table_layout
            cols: 4
            row_default_height: '30dp'
            MDLabel:
                text: 'Location Name'
            MDLabel:
                text: 'Longitude'
            MDLabel:
                text: 'Latitude'
            MDLabel:
                text: 'Image'
    MDRoundFlatButton:
        text: "Go to Locations Screen"
        pos_hint: {"center_x": .5}
        font_size: 20
        on_press: root.manager.current='adminmenu'

<ViewCategory>:
    name: 'viewcategory'
    cols: 2  # Set the number of columns
    ScrollView:
        GridLayout:
            id: category_table_layout
            cols: 2
            MDLabel:
                text: 'Category Name'
            MDLabel:
                text: 'Image'
    MDRoundFlatButton:
        text: "Go to Category Screen"
        pos_hint: {"center_x": .5}
        font_size: 20
        on_press: root.manager.current='adminmenu'
"""