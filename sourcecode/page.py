from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def root():
  return render_template('page.html'), 200

# Guitar page. Importing data from json file and sending it to the template.
@app.route('/guitars/')
def guitars():
  data = {}   #set data to empty dict in case the json file is empty
  import json
  try:  #read from json file if not empty
    with open('static/data.json', 'r') as f:
      data = json.load(f)
  except:
    pass

  return render_template('guitars.html',data=data['guitars']), 200

# Page for adding guitars to the list
@app.route('/guitars/add', methods=['POST','GET'])
def addguitar():
  data = {}
  import json
  try:
    with open('static/data.json', 'r') as f:
      data = json.load(f)
  except:
    pass

  #recover data from user input
  if request.method == 'POST':
    f = request.files['photo']
    print request.form
    brand = request.form['brand']
    model = request.form['model']
    desc = request.form['desc']
    id = 1;   #set initially in case json file is empty
    try:    #set id equal to number of objects in guitars array, plus 1 
      id = len(data['guitars']) + 1
    except:
      pass

    #set photo name as id number and save 
    photo = '%s.jpg' % id
    f.save('static/uploads/guitars/%s.jpg' % id)

    #save the guitar to a dict and append to guitars array
    newguitar = { 'id' : id, 'brand' : brand, 'model' : model, 'desc' : desc,
      'photo' : photo }
    data['guitars'].append(newguitar)
    with open('static/data.json', 'w') as outfile:
      json.dump(data, outfile)

    #return to guitars page
    return render_template('guitars.html', data=data['guitars']), 200
  else:
    return render_template('guitaradd.html'), 200

#page for filtering guitars, using jinja
@app.route('/guitars/filter/<filter>')
def guitarfilter(filter=None):
  import json
  try:
    with open('static/data.json', 'r') as f:
      data = json.load(f)
  except:
    pass
  #make empty list
  filtered = []

  #iterate through all guitars and filter
  for item in data["guitars"]:
    if item["brand"] == filter.title():
      filtered.append(item)

  #send filtered list to template for displaying
  return render_template('guitars.html', data=filtered), 200

#page for filtering amps
@app.route('/amps/filter/<filter>')
def ampfilter(filter=None):
  import json
  try:
    with open('static/data.json', 'r') as f:
      data = json.load(f)
  except:
    pass
  filtered = []
  for item in data["amps"]:
    if item["brand"] == filter.title():
      filtered.append(item)

  return render_template('amps.html', data=filtered), 200

#page for filtering effects
@app.route('/effects/filter/<filter>')
def effectfilter(filter=None):
  import json
  try:
    with open('static/data.json', 'r') as f:
      data = json.load(f)
  except:
    pass
  filtered = []
  for item in data["effects"]:
    if item["brand"] == filter.title():
      filtered.append(item)

  return render_template('effects.html', data=filtered), 200

#amps page
@app.route('/amps/')
def amps():
  data = {}
  import json
  try:
    with open('static/data.json', 'r') as f:
      data = json.load(f)
  except:
    pass

  return render_template('amps.html',data=data['amps']), 200

#page for adding amps
@app.route('/amps/add', methods=['POST','GET'])
def addamp():
  data = {}
  import json
  try:
    with open('static/data.json', 'r') as f:
      data = json.load(f)
  except:
    pass
  if request.method == 'POST':
    f = request.files['photo']
    print request.form
    brand = request.form['brand']
    model = request.form['model']
    desc = request.form['desc']
    id = 1;
    try:
      id = len(data['amps']) + 1
    except:
      pass
    photo = '%s.jpg' % id
    f.save('static/uploads/amps/%s.jpg' % id)
    newamp = { 'id' : id, 'brand' : brand, 'model' : model, 'desc' : desc,
      'photo' : photo }

    data['amps'].append(newamp)
    with open('static/data.json', 'w') as outfile:
      json.dump(data,outfile)

    return render_template('amps.html',data=data['amps']), 200
  else:
    return render_template('ampadd.html'), 200

#effects page
@app.route('/effects/')
def effects():
  data = {}
  import json
  try:
    with open('static/data.json', 'r') as f:
      data = json.load(f)
  except:
    pass

  return render_template('effects.html',data=data['effects']), 200

#page for adding effects
@app.route('/effects/add', methods=['POST','GET'])
def add():
  data = {}
  import json
  try:
    with open('static/data.json', 'r') as f:
      data = json.load(f)
  except:
    pass
  if request.method == 'POST':
    f = request.files['photo']
    print request.form
    brand = request.form['brand']
    model = request.form['model']
    desc = request.form['desc']
    id = 1;
    try:
      id = len(data['effects']) + 1
    except:
      pass
    photo = '%s.jpg' % id
    f.save('static/uploads/effects/%s.jpg' % id)
    neweffect = { 'id' : id, 'brand' : brand, 'model' : model, 'desc' : desc,
      'photo' : photo }

    data['effects'].append(neweffect)
    with open('static/data.json', 'w') as outfile:
      json.dump(data, outfile)

    return render_template('effects.html',data=data['effects']), 200
  else:
    return render_template('effectadd.html'), 200

@app.route('/guitars/single/<zoom>')
def guitarzoom(zoom=None):
  import json
  try:
    with open('static/data.json', 'r') as f:
      data = json.load(f)
  except:
    pass
  single = []
  for item in data["guitars"]:
    if item["id"] == int(zoom):
      single = item

  return render_template('guitarzoom.html', data=single), 200

@app.route('/amps/single/<zoom>')
def ampzoom(zoom=None):
  import json
  try:
    with open('static/data.json', 'r') as f:
      data = json.load(f)
  except:
    pass
  single = []
  for item in data["amps"]:
    if item["id"] == int(zoom):
      single = item

  return render_template('ampzoom.html', data=single), 200

@app.route('/effects/single/<zoom>')
def effectzoom(zoom=None):
  import json
  try:
    with open('static/data.json', 'r') as f:
      data = json.load(f)
  except:
    pass
  single = []
  for item in data["effects"]:
    if item["id"] == int(zoom):
      single = item

  return render_template('effectzoom.html', data=single), 200

#about page
@app.route('/about/')
def about():
  return render_template('about.html'), 200

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
