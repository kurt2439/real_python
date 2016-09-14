birthdays = {}
birthdays['Luke Skywalker'] = '5/24/19'
birthdays['Obi-Wan Kenobi'] = '3/11/57'
birthdays['Darth Vader'] = '4/1/41'

if 'Yoda' not in birthdays:
    birthdays['Yoda'] = 'unknown'

if 'Darth Vader' not in birthdays:
    birthdays['Darth Vader'] = 'unknown'

for jedi in birthdays:
    print(jedi,birthdays[jedi])

del( birthdays['Darth Vader'] )

for jedi in birthdays:
    print(jedi,birthdays[jedi])

sw_dict = dict([('Luke Skywalker','5/7/2010'), ('Han Solo','2/5/1945')])

for character in sw_dict:
    print(character, sw_dict[character] )
