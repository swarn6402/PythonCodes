file = open('youtube.txt', 'w')

try:
    file.write('India vs England')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('India vs Australia')