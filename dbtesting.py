import hashlib

def hash_string(string):
    # Hash la chaîne de caractères en utilisant SHA-256
    hashed_string = hashlib.sha256(string.encode()).hexdigest()
    return hashed_string

# Exemple d'utilisation de la fonction
string_to_hash = "1308"
hashed_result = hash_string(string_to_hash)
print("Le hash de la chaîne '{}' est : {}".format(string_to_hash, hashed_result))
