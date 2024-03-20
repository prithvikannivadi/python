# Return user provided input, replacing ":)" or ":(" with the appropriate emoticon

faces = input('Provide a sentence, including ":)" or ":(". ')

face = faces.replace(":)" , "🙂")
facez = face.replace(":(" , "🙁")

print (facez)
