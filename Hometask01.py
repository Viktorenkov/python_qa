#Hometask01
#norway_text = 'Automatisering akselererer %syeblikket da roboter vil erobre planeten v%sr. (%s)' % ('ø', 'å', 'Æ')
#print(norway_text)

#1

norway_text = f'Automatisering akselererer {'ø'}syeblikket da roboter vil erobre planeten v{'å'}sr. ({'Æ'}s)'

print(norway_text)

#2
format_norway_text = ('Automatisering akselererer {0}syeblikket da roboter vil erobre ' 
              'planeten v{1}sr. ({2}s)'.format('ø', 'å', 'Æ'))

print(format_norway_text)