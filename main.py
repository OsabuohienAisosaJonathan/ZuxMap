from kivymd.app import MDApp
from kivy_garden.mapview import MapView

class MapView(MDApp):
    def build(self):
        mapview = MapView(zoom=10, Lat=36, Lon=-115)
        return mapview

MapView().run()
