from kivymd.app import MDApp
import boto3
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from screen_nav import screen_helper
import pymysql
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty
from kivymd.toast import toast
from kivy.core.window import Window
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.label import MDLabel
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
import os
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
Bucket_Name = "mobileappbucket-new"
s3_client = boto3.client('s3', aws_access_key_id="AKIA4WFGH2B7OWNMKKU4", aws_secret_access_key="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")

conn = pymysql.connect(host="appdatabase.czrro6tu6hbs.us-east-2.rds.amazonaws.com", user="admin", password="admin123", db="SnowRemovalApp")
cursor = conn.cursor()

Window.size = (450, 580)


class TopPage(Screen):
    pass


class MenuScreen(Screen):

    def admin_login(self):
        admin_email = self.admin_email.text
        admin_password = self.admin_password.text
        if admin_email == 'admin@gmail.com' and admin_password == 'admin':
            self.manager.current = 'adminhome'
            toast("Login Successfull")
        else:
            toast("Invalid Login Details")

        self.admin_email.text = ''
        self.admin_password.text = ''

class AdminHome(Screen):
    pass

class AdminScreen(Screen):
    location_name = ObjectProperty(None)
    longitude = ObjectProperty(None)
    latitude = ObjectProperty(None)
    category_name = ObjectProperty(None)

    def add_location_data(self):
        location_name = self.location_name.text
        longitude = self.longitude.text
        latitude = self.latitude.text
        location_picture = self.ids.location_picture.source
        location_file_name = os.path.basename(location_picture)
        s3_client.upload_file(location_picture, Bucket_Name, location_file_name)
        bucket_name = 'mobileappbucket-new'
        s3_file_name = location_file_name

        location_image_url = f'https://{bucket_name}.s3.amazonaws.com/{s3_file_name}'
        count = cursor.execute("select * from location where location_name = '" + str(location_name) + "'")
        if count == 0:
            query = ("insert into location(location_name,longitude,latitude,location_picture) values('" + str(location_name) + "' , '" + str(longitude) + "' , '" + str(latitude) + "' , '" + str(location_image_url) + "')")
            cursor.execute(query)
            conn.commit()
            toast("Location Added Successfull")
        else:
            toast("Duplicate Details")

        self.location_name.text = ''
        self.longitude.text = ''
        self.latitude.text = ''
        self.ids.location_picture.source = ''

    def location_button(self):
        from plyer import filechooser
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        self.ids.location_picture.source = selection[0]
        toast("Location Picture Selected")

    def view_locations(self):
        self.manager.current = "viewlocations"

    def add_category_data(self):
        category_name = self.category_name.text
        category_picture = self.ids.category_image.source
        category_file_name = os.path.basename(category_picture)
        s3_client.upload_file(category_picture, Bucket_Name, category_file_name)
        bucket_name = 'mobileappbucket-new'
        s3_file_name = category_file_name

        category_image_url = f'https://{bucket_name}.s3.amazonaws.com/{s3_file_name}'
        count = cursor.execute("select * from category where category_name = '" + str(category_name) + "'")
        if count == 0:
            query = ("insert into category(category_name,category_picture) values('" + str(category_name) + "' , '" + str(category_image_url) + "')")
            cursor.execute(query)
            conn.commit()
            toast("Category Added Successfull")
        else:
            toast("Duplicate Details")

        self.category_name.text = ''
        self.ids.category_picture.source = ''

    def category_button(self):
        from plyer import filechooser
        filechooser.open_file(on_selection=self.category_selected)

    def category_selected(self, selection):
        self.ids.category_image.source = selection[0]
        toast("Category Image Selected")

    def view_category(self):
        self.manager.current = "viewcategory"

    def __init__(self, **kwargs):
        super(AdminScreen, self).__init__(**kwargs)
        Clock.schedule_once(self.populate_table)

    def populate_table(self, *args):
        self.cols = 2
        provider_table_layout = self.ids['provider_table_layout']
        cursor.execute("SELECT name,email,phone,password,address,profile_picture,license,id_proof,status FROM service_provider")
        service_providers = cursor.fetchall()
        for service_provider in service_providers:
            name = service_provider[0]
            email = service_provider[1]
            phone = service_provider[2]
            password = service_provider[3]
            address = service_provider[4]
            profile_picture = service_provider[5]
            license = service_provider[6]
            id_proof = service_provider[7]
            status = service_provider[8]

            name = MDLabel(text=name)
            email = MDLabel(text=email)
            phone = MDLabel(text=phone)
            password = MDLabel(text=password)
            address = MDLabel(text=address)
            profile_picture = AsyncImage(source=profile_picture)  # Create a new AsyncImage
            license = AsyncImage(source=license)
            id_proof = AsyncImage(source=id_proof)
            status = MDLabel(text=status)

            provider_table_layout.add_widget(name)
            provider_table_layout.add_widget(email)
            provider_table_layout.add_widget(phone)
            provider_table_layout.add_widget(password)
            provider_table_layout.add_widget(address)
            provider_table_layout.add_widget(profile_picture)
            provider_table_layout.add_widget(license)
            provider_table_layout.add_widget(id_proof)
            provider_table_layout.add_widget(status)

class ViewLocations(Screen):
    def __init__(self, **kwargs):
        super(ViewLocations, self).__init__(**kwargs)
        Clock.schedule_once(self.populate_table)

    def populate_table(self, *args):
        self.cols = 4
        try:
            location_table_layout = self.ids['location_table_layout']
            cursor.execute("SELECT location_name,longitude,latitude,location_picture FROM location")
            locations = cursor.fetchall()
            for location in locations:
                location_name = location[0]
                longitude = location[1]
                latitude = location[2]
                location_picture = location[3]

                location_name = MDLabel(text=location_name)
                longitude = MDLabel(text=longitude)
                latitude = MDLabel(text=latitude)
                location_picture = AsyncImage(source=location_picture)

                location_table_layout.add_widget(location_name)
                location_table_layout.add_widget(longitude)
                location_table_layout.add_widget(latitude)
                location_table_layout.add_widget(location_picture)
        except Exception as e:
            print(f"An error occurred: {e}")

class ViewCategory(Screen):
    def __init__(self, **kwargs):
        super(ViewCategory, self).__init__(**kwargs)
        Clock.schedule_once(self.populate_table)

    def populate_table(self, *args):
        self.cols = 2
        category_table_layout = self.ids['category_table_layout']
        cursor.execute("SELECT category_name,category_picture FROM category")
        categories = cursor.fetchall()
        for category in categories:
            category_name = category[0]
            category_picture_path = category[1]

            category_name_label = MDLabel(text=category_name)
            category_image = AsyncImage(source=category_picture_path,size=(30, 30))  # Create a new AsyncImage

            category_table_layout.add_widget(category_name_label)
            category_table_layout.add_widget(category_image)


class CustomerRegistration(Screen):

    fname = ObjectProperty(None)
    email= ObjectProperty(None)
    phone= ObjectProperty(None)
    password= ObjectProperty(None)
    address= ObjectProperty(None)
    longitude= ObjectProperty(None)
    latitude= ObjectProperty(None)

    def send_data(self):
        fname = self.fname.text
        email =  self.email.text
        phone =  self.phone.text
        password =  self.password.text
        address =  self.address.text
        longitude =  self.longitude.text
        latitude = self.latitude.text
        count = cursor.execute("select * from customer where email = '"+str(email)+"' or phone = '"+str(phone)+"'")
        if count == 0:
            query = ("insert into customer(name,email,phone,password,address,longitude,latitude) values('" + str(fname) + "' , '" + str(email) + "' , '" + str(phone) + "' , '" + str(password) + "' , '" + str(address) + "' , '" + str(longitude) + "' , '" + str(latitude) + "')")
            cursor.execute(query)
            conn.commit()
            toast("Registration Successfull")
        else:
            toast("Duplicate Details")
        self.fname.text = ''
        self.email.text = ''
        self.phone.text = ''
        self.password.text = ''
        self.address.text = ''
        self.longitude.text = ''
        self.latitude.text = ''


class ServiceProviderReg(Screen):

    sname = ObjectProperty(None)
    email = ObjectProperty(None)
    phone = ObjectProperty(None)
    password = ObjectProperty(None)
    address = ObjectProperty(None)

    def register_data(self):
        sname = self.sname.text
        email = self.email.text
        phone = self.phone.text
        password = self.password.text
        address = self.address.text
        profile = self.ids.profile_img.source
        license = self.ids.licence_img.source
        idproof = self.ids.id_proof_img.source
        profile_file_name = os.path.basename(profile)
        license_file_name = os.path.basename(license)
        idproof_file_name = os.path.basename(idproof)
        s3_client.upload_file(profile, Bucket_Name, profile_file_name)
        s3_client.upload_file(license, Bucket_Name, license_file_name)
        s3_client.upload_file(idproof, Bucket_Name, idproof_file_name)
        bucket_name = 'mobileappbucket-new'
        s3_file_name = profile_file_name
        s3_file_name_license = license_file_name
        s3_file_name_idproof = idproof_file_name

        profile_image_url = f'https://{bucket_name}.s3.amazonaws.com/{s3_file_name}'
        license_image_url = f'https://{bucket_name}.s3.amazonaws.com/{s3_file_name_license}'
        idproof_image_url = f'https://{bucket_name}.s3.amazonaws.com/{s3_file_name_idproof}'
        count = cursor.execute("select * from service_provider where email = '" + str(email) + "' or phone = '" + str(phone) + "'")
        if count == 0:
            query = ("insert into service_provider(name,email,phone,password,address,profile_picture,license,id_proof,status) values('" + str(sname) + "' , '" + str(email) + "' , '" + str(phone) + "' , '" + str(password) + "' , '" + str(address) + "' , '" + str(profile_image_url) + "' , '" + str(license_image_url) + "' , '" + str(idproof_image_url) + "' , 'Deactivate')")
            cursor.execute(query)
            conn.commit()
            toast("Registration Successfull")
        else:
            toast("Duplicate Details")
        self.sname.text = ''
        self.email.text = ''
        self.phone.text = ''
        self.password.text = ''
        self.address.text = ''
        self.ids.profile_img.source = ''
        self.ids.licence_img.source = ''
        self.ids.id_proof_img.source = ''

    def profile_button(self):
        from plyer import filechooser
        filechooser.open_file(on_selection = self.selected)

    def selected(self, selection):
        self.ids.profile_img.source = selection[0]
        toast("Profile Selected")

    def licence_button(self):
        from plyer import filechooser
        filechooser.open_file(on_selection = self.licence_selected)

    def licence_selected(self, selection):
        self.ids.licence_img.source = selection[0]
        toast("Licence Uploaded")

    def id_proof_button(self):
        from plyer import filechooser
        filechooser.open_file(on_selection = self.id_proof_selected)

    def id_proof_selected(self, selection):
        self.ids.id_proof_img.source = selection[0]
        toast("ID Proof Selected")


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Snow Removal App"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_string(screen_helper)
        self.manager = ScreenManager(transition=NoTransition())
        self.manager.add_widget(TopPage(name="toppage"))
        self.manager.add_widget(MenuScreen(name="menu"))
        self.manager.add_widget(CustomerRegistration(name="c    ustomerreg"))
        self.manager.add_widget(ServiceProviderReg(name="serviceproviderreg"))
        self.manager.add_widget(AdminHome(name="adminhome"))
        self.manager.add_widget(AdminScreen(name="adminmenu"))
        self.manager.add_widget(ViewLocations(name="viewlocations"))
        self.manager.add_widget(ViewCategory(name="viewcategory"))

    def customerreg(self):
        self.manager.current = "customerreg"

    def serviceproviderreg(self):
        self.manager.current = "serviceproviderreg"

    def viewlocations(self):
        self.manager.current = "viewlocations"

    def viewcategory(self):
        self.manager.current = "viewcategory"



if __name__ == "__main__":
    MainApp().run()