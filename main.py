# finding names
from pyscript import display, document


def name_finder (e):
   document.getElementById('result').innerHTML = ' '

   first_name = document.getElementById('firstname').value.title().strip()
   last_name = document.getElementById('surname').value.title().strip()
   cool_kids_members = first_name + " " + last_name


   members = ["Franco Deocampo", "Aisha Padua", "Cassandra Dazo", "Sito Policarpio", "Nicolo Sleepyboy", "Almakram Arbison", "Keane Pacaña", "Sebastian Uclaray", "Izzy Herrera", "Ford Aj Variant",]


   acceptance_checker = cool_kids_members in members


   display_message = (f'We regret to inform you that {cool_kids_members} has not been accepted into the Cool Kids de Manila University.', f'Congratulations! We are pleased to inform you that {cool_kids_members} has been accepted into the Cool Kids de Manila University!')
   display(display_message[acceptance_checker], target='result')

