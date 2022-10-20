class CPU:

    def __init__(self, name, model, brand, msrp, tdp, release_date):
        self.name = name
        self.model = model
        self.brand = brand
        self.msrp = msrp
        self.tdp = tdp
        self.release_date = release_date

    def get_name(self):
        return self.name

    def get_model(self):
        return self.model

    def get_brand(self):
        return self.brand

    def get_msrp(self):
        return self.msrp

    def get_tdp(self):
        return self.tdp

    def get_release_date(self):
        return self.release_date

    def get_all(self):
        return self.get_name(), self.get_model(), self.get_brand(), self.get_msrp(), self.get_tdp(),\
        self.get_release_date()
