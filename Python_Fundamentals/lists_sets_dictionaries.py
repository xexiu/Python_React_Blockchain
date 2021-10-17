colors = ['red', 'yellow', 'blue']
neutral_colors = ['white', 'black']
colors.append('green')
# ['red', 'yellow', 'blue', 'green']
colors.extend(neutral_colors)
# ['red', 'yellow', 'blue', 'green', 'white', 'black']
colors.remove('blue')
# ['red', 'yellow', 'green', 'white', 'black']
colors.pop() # last item > 'black'
colors.sort() # sorts the array

# Whitin arrays you can have duplicates
days = ['Monday', 'Sunday', 'Friday', 'Tuesday', 'Monday', 'Friday']
# ['Monday', 'Sunday', 'Friday', 'Tuesday', 'Monday', 'Friday']

# Whitin sets (object declaration), you can't have duplicates
days = { 'Monday', 'Sunday', 'Friday', 'Tuesday', 'Monday', 'Friday' }
# { 'Monday', 'Sunday', 'Friday', 'Tuesday' }

'Monday' in days # True
days.add('Wednesday') # Add method for sets

grades = {'Sam': 20, 'Beth': 33}
grades['John'] = 40
# { 'Sam': 20, 'Beth': 33, 'John': 40 }
del grades['Sam']
# { 'Beth': 33, 'John': 40 }
grades.keys()
# dict_keys('Beth', 'John')
list(grades.keys())
# ['Sam', 'John']
grades.values()
# dict_values([33, 40])

