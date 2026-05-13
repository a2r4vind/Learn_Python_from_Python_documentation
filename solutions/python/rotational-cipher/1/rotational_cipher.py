def rotate(text, key):
    if key in (0, 26):
        return text

    ciper_txt = ""

    if key in range(1, 26):
        
        for char in text:
            
            if char.isalpha():
                start_position = ord('A') if char.isupper() else ord('a')
                new_char = chr((ord(char) - start_position + key) % 26 + start_position)
                ciper_txt += new_char
            else:
                ciper_txt += char

        return ciper_txt

    else:
        raise ValueError('Key should be between 0 and 26')
                
            
