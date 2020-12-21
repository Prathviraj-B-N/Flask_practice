from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return '''<h1>Adopt a Pet!</h1>
            <p>Browse through the links below to find your new furry friend:</p>
            <ul>
            <li><a href = "/animals/Dogs">Dogs</a></li>
            <li><a href = "/animals/Cats">Cats</a></li>
            <li><a href = "/animals/Rabbits">Rabbits</a></li>
            </ul>'''

@app.route('/animals/<pet_type>')
def animals(pet_type):
  pet_list = pets[pet_type.lower()]
  strx = ''

  for each in pet_list:
    strx += '<ul>'
    for x,y in each.items():
      if x == 'url':
        strx +='<li><a href='+str(y)+'>[img]</a>'
        continue
      strx +='<li>'+str(x)+' : '+str(y)
    strx += '</ul><br>'

    
  return '''<h1>List of {p_type}</h1>
  {lists}
  '''.format(p_type = pet_type,lists = strx)
