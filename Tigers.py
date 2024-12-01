# Import the Animal class from the Animal module
from AnimalClasses import Animal

class Tiger(Animal):
    # create a static class variable to keep track of the number of hyenas created
    numOfTigers = 0

    # Create the hyena sound
    tiger_sound = " meow...meow "

    # Create a list of hyena names.
    list_of_tiger_names = []

    file_path = r'C:\Users\Ari\CIT95\ZookeeperChallenge\animalNames.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Iterate through the lines in the file
        line_num = 1
        for line in lines:
            if line_num == 15:
                list_of_tiger_names.extend(line.strip().split(', '))
                break
            else:
                line_num += 1

    def __init__(self, name="a_name", animal_id="an_id", birth_date="2099-01-01", color="a_color", gender="a_gender",
                 weight="a_weight", originating_zoo="a_zoo", date_arrival="2099-01-01"):
        # Increment the static variable numOfHyenas when a new Hyena object is created
        Tiger.numOfTigers += 1

        # Call the constructor of the parent class (Animal) with 'Hyena' as the species
        super().__init__("tiger", name, animal_id, birth_date, color, gender, weight, originating_zoo, date_arrival)

    def make_sound(self):
        return self.tiger_sound

    # the tiger object will call this method to get an unused tiger name. pop() will remove the first element from
    #   the list_of_tiger_names[]
    def get_tiger_name(self):
        return self.list_of_tiger_names.pop(0)


