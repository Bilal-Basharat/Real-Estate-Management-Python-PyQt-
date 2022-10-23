# Properties BL CLass
class Property:
    AgencyName = ""
    Type = ""
    Price = ""
    Area = ""
    Purpose = ""
    City =""
    Contact = ""

    def __init__(self, AgencyName, Type, Price, Area, Purpose, City, Contact):
        self.AgencyName = AgencyName
        self.Type = Type
        self.Price = Price
        self.Area = Area
        self.Purpose = Purpose
        self.City = City
        self.Contact = Contact

        
        