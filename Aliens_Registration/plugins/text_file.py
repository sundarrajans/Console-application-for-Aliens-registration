from .. format import Format
class text_file(Format):
    def __init__(self,alien):
        self.alien = alien
    
    def create(self):
        """ method to create text file """
        name = self.alien.code_name+'.txt'
        try:
            f = open(name,'w')
            f.write('\t'*4 + 'REGISTRATION DETAILS\n')
            f.write('Code Name:  ' + self.alien.code_name + '\n' +
                'Blood Color:' +self.alien.blood_color + '\n' +
                'No of Antennas:  '+self.alien.no_of_antennas + '\n' +
                'No of Legs:  '+self.alien.no_of_legs + '\n' +
                'Home Planet:  '+self.alien.home_planet 
                   )
            f.close()
        except exception as e:
            print e
        return True
