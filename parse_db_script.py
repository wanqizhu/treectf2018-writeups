# parse the /db folder in the unzipped downloaded CTFD export

peeps = json.load(open('teams.json'))['results']
people = [(p['name'], p['email']) for p in peeps]

keys = json.load(open('keys.json'))['results']
flags = [(k['chal'], k['flag']) for k in keys]

chal = json.load(open('challenges.json'))['results']
for i in range(len(chal)):
  chal[i]['flag'] = flags[i]  # add flags and remove logistic fields
  chal[i].pop('id')
  chal[i].pop('max_attempts')
  chal[i].pop('type')
  chal[i].pop('hidden')

print(json.dumps(chal, indent=4))
