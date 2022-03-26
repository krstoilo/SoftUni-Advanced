class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date: str, age_restriction):
        date_list = date.split(".")
        creation_year = int(date_list[2])
        creation_month = ""
        if date_list[1] == "1":
            creation_month = "January"
        if date_list[1] == "2":
            creation_month = "February"
        if date_list[1] == "3":
            creation_month = "March"
        if date_list[1] == "4":
            creation_month = "April"
        if date_list[1] == "5":
            creation_month = "May"
        if date_list[1] == "6":
            creation_month = "June"
        if date_list[1] == "7":
            creation_month = "July"
        if date_list[1] == "8":
            creation_month = "August"
        if date_list[1] == "9":
            creation_month = "September"
        if date_list[1] == "10":
            creation_month = "October"
        if date_list[1] == "11":
            creation_month = "November"
        if date_list[1] == "12":
            creation_month = "December"
        return cls(name, id, creation_year, creation_month, age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction" \
               f" {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"