import re

new_string = 'Rose67lilly78Jasmine228Tulip'
new_result = re.findall('[0-9]+', new_string)
print(new_result)