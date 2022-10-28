

def cipher(text, shift, encrypt=True):
    """
    This fuction conducts Caesar cipher 
    Casser cipher is one of the simplest and mose widely known encryption techniques. 
    Each letter is replaced by a letter some fixed number of positions down (encryptiont) or up (decription) the alphabet.

    Parameters
    ----------
    text : sting letter text 
    shift : the number of position down the alphabet
    encrypt : boolean value (default : True)
            True, the function is run by encryption 
            False, the functio is run by decryption 
    
    Returns
    -------
    string 
       New text encrypted (in case of encription) or decrypted

    Examples
    --------
    >>> text = "I am a boy."
    >>> cipher(text = text, shift = 1, encrypt=True)
    'J bn b cpz.'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

