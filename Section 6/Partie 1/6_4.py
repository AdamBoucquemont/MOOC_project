def substitue(message, abreviation):
    new_message = []
    for word in message.split():
        if word in abreviation:
            new_message.append(abreviation[word])
        else:
            new_message.append(word)
    return " ".join(new_message)

message = 'C. N. cpt 2 to inf'
abreviation = {'C.' : 'Chuck',
    'N.' : 'Norris',
    'cpt' : 'counted',
    '2' : 'two times',
    'inf' : 'infinity'}
print(substitue(message, abreviation))