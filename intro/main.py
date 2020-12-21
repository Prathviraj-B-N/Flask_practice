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
@app.route('/animals/')
def animals(pet_type):
  pet_list = pets[pet_type.lower()]
  strx = ''

  strx += '<ul>'
  for idx,each in enumerate(pet_list):
    strx +='<li>'+'<a href = "/animals/'+str(pet_type)+'/'+str(idx)+'">'+str(each['name'])+'</a>'
  strx += '</ul>'

    
  return '''<h1>List of {p_type}</h1>
  {lists}
  '''.format(p_type = pet_type,lists = strx)

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type,pet_id):
  pet = pets[pet_type.lower()][pet_id]
  return '''
  <h1>{name}</h1>
  <img src="{img_url}" alt="{name}" width="500" height="600">
  <p>{info}</p>
  <ul>
    <li>{breed}
    <li>{age}
  </ul>
  
  '''.format(name = pet['name'],img_url=pet['url'],info = pet['description'],breed=pet['breed'],age = pet['age'])

