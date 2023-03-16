pupils = [
    {
          'firstname': 'Valera',
          'group': 42,
          'phis': 7,
          'inf': 4,
          'mats': 2
           },
          {
              'firstname': 'Ritta',
          'group': 42,
          'phis': 10,
          'inf': 6,
          'mats': 5,
           },
          {
              'firstname': 'Oleg',
          'group': 42,
          'phis': 8,
          'inf': 8,
          'mats': 7
          }
          ]
for data in pupils:
    avg_student = (data['phis'] + data['inf'] + data['mats']) / 3
    if avg_student > 6:
        print(data)