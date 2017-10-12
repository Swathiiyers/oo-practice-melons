############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""
        self.code  = code
        self.name = name
        self.first_harvest =  first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.pairings = []



    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""


        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.new_code = new_code




def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    melon = MelonType('musk', 'Muskmelon', 1998, 'green', True, True)
    melon.add_pairing('mint')
    all_melon_types.append(melon)

    casaba = MelonType('cas', 'Casaba', 2003, 'orange', False, False)
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 'Crenshaw', 1996, 'green', False, False)
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType('yw', 'Yellow Watermelon', 2013, 
        'yellow', False, True)
    yellow_watermelon.add_pairing('ice_cream')
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairings(melons_list):
    """takes the list of MelonType objects,
    and prints out the pairs for each object
    """
    for melon in melons_list:
        print "\n{} pairs with ".format(melon.name)
        for i in range(len(melon.pairings)):
            print "- {}".format(melon.pairings[i])


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melons_dict = {}

    for melon in melon_types:
        melons_dict[melon.code] = melon

    return melons_dict




############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_day, melon_type, shape_rating, color_rating, harvest_field_num, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_field_num = harvest_field_num
        self.harvested_by = harvested_by

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def is_sellable(self,shape_rating,color_rating):
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        if self.shape_rating > 5 and self.color_rating >5:
            return True
        else:
            return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_new_list = []

    Melon1 = Melon(melon_types['yw'], 8, 7, 2, 'Sheila')
    melons_new_list.append(Melon1)

    Melon2 = Melon()




    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 

all_melons = make_melon_types()
print_pairings(all_melons)
melons_dictionary = make_melon_type_lookup(all_melons)
make_melons(all_melons)
