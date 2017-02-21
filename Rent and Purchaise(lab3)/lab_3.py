class Property:
    """class will collect input information and printing some useful"""
    def __init__(self, square_feet='', beds='',
                 baths='', **kwargs):  # adding a **kwargs variable, in case that it is going to be used multiple times
        self.square_feet = square_feet
        self.num_bedrooms = beds  # giving a variable`s
        self.num_baths = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """method will collect input information"""
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)  # creating a global variable


class Apartment(Property):
    """the Apartment class extends Property, and is similar in structure"""
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):  # __init__ method call their respective parent class method`s
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):  # display method ensure that Property class is properly initialized
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)
        parent_init = Property.prompt_init()
        laundry = ''  # giving an information about type of apartment
        while laundry.lower() not in Apartment.valid_laundries:
            laundry = input("What laundry facilities does "
                            "the property have? ({})".format(
                            ", ".join(Apartment.valid_laundries)))
        balcony = ''
        while balcony.lower() not in Apartment.valid_balconies:
            balcony = input("Does the property have a balcony? "
                            "({})".format(", ".join(Apartment.valid_balconies)))
            parent_init.update({"laundry": laundry, "balcony": balcony})
        return parent_init

    def prompt_init():
        """getting dictionary values from the parent class, and then adding some additional values of its own."""
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry facilities does "
            "the property have? ",
            Apartment.valid_laundries)
        balcony = get_valid_input(
            "Does the property have a balcony? ",
            Apartment.valid_balconies)
        parent_init.update({"laundry": laundry, "balcony": balcony})
        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    """This class has a parallel structure to Apartment, but refers to different prompts and variables."""
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='',
                 garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        super().display()
        print("HOUSE DETAILS")  # func gives information about house stats
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)  # extra stats, for potential buyer
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    """Haven`t any superclasses, but can call super.__init__ because it gonna combine whit other classes"""
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))
        # information about apartment price
    def prompt_init():
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? "))

    prompt_init = staticmethod(prompt_init)


class Rental:
    """same stats as in Purchase class"""
    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(
            self.utilities))
        print("furnished: {}".format(self.furnished))
        # information about rent price
    def prompt_init():
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input(
                "What are the estimated utilities? "),
            furnished=get_valid_input(
                "Is the property furnished? ",
                ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    """updating an House used with prompt_init() method"""
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):  # checking for the right input
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class ApartmentRental(Rental, Apartment):  # cost of apartment rent
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):  # cost of apartment purchase
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):  # cost of house purchase
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class Agent:
    """class Agent is responsible for creating new listings and displaying existing ones"""
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()

    def add_property(self):  # an extra information for agent
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()
        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))
