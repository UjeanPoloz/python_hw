full_info = 'Marcus Aurelius*121-04-26*180-03-17'

split_info = full_info.split('*')

birth_date = split_info[1]
death_date = split_info[2]

split_birth_date = birth_date.split('-')
split_death_date = death_date.split('-')

age = int(split_death_date[0]) - int(split_birth_date[0])

print('Full info:  %s\n \n'
      'Short line: %s, %s' % (full_info, split_info[0],age))

