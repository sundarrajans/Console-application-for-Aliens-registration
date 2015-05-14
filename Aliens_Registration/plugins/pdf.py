from reportlab.pdfgen import canvas
from ..format import Format
class pdf(Format):
    def __init__(self,alien):
        self.alien = alien

        
    def create(self):
        """ method to create pdf """
        pdf_name = self.alien.code_name + '.pdf'
        try:
            c = canvas.Canvas(pdf_name,bottomup = 0)
            c.setLineWidth(.3)
            c.setFont('Helvetica', 12)
            c.drawString(200, 10,"REGISTRATION DETAILS")
            c.line(30,30, 750,30)
            c.drawString(30,50, 'Code Name:  '+self.alien.code_name)
            c.drawString(30,70, 'Blood Color:  '+self.alien.blood_color)
            c.drawString(30,90, 'No of Antennas:  '+self.alien.no_of_antennas)
            c.drawString(30,110, 'No of Legs:  '+self.alien.no_of_legs)
            c.drawString(30,130, 'Home Planet:  '+self.alien.home_planet)
            c.save()
        except Exception as e:
            raise e
        return True
