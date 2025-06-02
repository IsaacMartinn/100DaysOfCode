from logo import logo

alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
    "u", "v", "w", "x", "y", "z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
    "u", "v", "w", "x", "y", "z"
]

print(logo)
game_on = True
while game_on: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def ceaser(direction,text,shift):
        
            if direction == "encode":
                def encrypt(original_text, shift_amount):
                    cipher_text = ""

                    for letter in original_text:
                        shifted_position = alphabet.index(letter) + shift_amount
                        cipher_text += alphabet[shifted_position]
                    
                    print(f"Here is the encoded result: {cipher_text}")

                encrypt(original_text=text,shift_amount=shift)


            elif direction == "decode":
                
                def decrypt(original_text, shift_amount):
                    """decodes the message to the original text"""
                    output_text = ""

                    for letter in original_text:
                        shifted_position = alphabet.index(letter) - shift_amount
                        output_text += alphabet[shifted_position]
                    
                    print(f"Here is the decoded result: {output_text}")



                decrypt(original_text=text,shift_amount=shift)
            

            

    ceaser(direction=direction, text=text, shift=shift)
    keep_playing = input("Do you want to continue? Type 'yes' or 'no'. ")
    if keep_playing == 'no':
         game_on = False
         print("Thank you for playing!")