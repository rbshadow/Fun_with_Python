def encode(string):
    ret_string = ''
    for i in string:
        asc = ord(i)
        asc -= 2
        if asc == 30:
            asc = 35
        ret_string += chr(asc)
    return ret_string


def decode(string):
    ret_string = ''
    for i in string:
        character = ord(i)
        character += 2
        if character == 35:
            character = 30
        ret_string += chr(character)
    return ret_string


i_put = input('Choose Option:' + '\n' + '1. Encode a string' + '\n' + '2. Decode a string' + '\n')

if int(i_put) == 1:
    enc_de = input()
    print('Encoded String is:')
    print(encode(enc_de))

elif int(i_put) == 2:
    dec_de = input()
    print('Decoded string is:')
    first_phase = decode(dec_de)
    decoded = first_phase.replace('%', ' ')
    print(decoded)
