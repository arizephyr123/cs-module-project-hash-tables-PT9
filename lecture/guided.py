    # return len(str)
## a lot of collisions

def UTF8_hash(str):
    # for letter in string:
        # val = ord(letter)
        # total += val
    total = 0
    UTF8_bytes = str.encode()
    for byte in UTF8_bytes:
        total += byte
        return total

# print(UTF8_hash('sad'))
# print(UTF8_hash('was'))

# better but will still have collisions:
print(UTF8_hash('add'))
print(UTF8_hash('dad'))

print(UTF8_hash('supercalifragilisticexpialodocious')) ## 3???

# operate on the bytes that make up the string
# Deterministic

# to improve hash function, make input more unique

# hash function + array
## hash function gives us back some big number
### how to map the output of our hash function to an index in an array

# before
# my_arr2 = [None] * 20

# idx = UTF8_hash('supercalifragilisticexpialodocious')
# my_arr2[idx] = 'Mary Poppins'

## how to turn the result




my_arr2 = [None] * 20

our_hash = UTF8_hash('supercalifragilisticexpialodocious')
idx = our_hash % len(my_arr2)
my_arr2[idx] = 'Mary Poppins'

print(my_arr2)


# Pseudocode for get:
### 1. Hash the key
### 2. Take the hash and mod it with the length of the array
### 3. Go to index and get out the value

# Pseudocode for put:
### 1. 
### 2. 
### 3. 

# Time complexity?
### linear


## Collision
key1 = 'add' # 
key2 = 'dad' #

### Get



### Put 1
hash1 = UTF8_hash(key1)
idx1 = hash1 % len(my_arr2)
my_arr2[idx1] = 'howdy'
print(my_arr2[idx1])

### Put 2 -> overrides 'howdy
hash2 = UTF8_hash(key2)
idx2 = hash2 % len(my_arr2)
my_arr2[idx2] = 'whats up yall'
print(my_arr2[idx2])


## Even when we use our hash function with modulo, we get collisions
### to be solved later

# We wrote our own hash function, what about Python's hash()?
### MAny different hash functions

# When used with ahs tables, hashing function should be FAST
### Why? we want 0(1), and a lot of lookups

## Other uses of hash functions
### passwords! e.g. bcryptjs
### encryption/ decryption

## password --> hashing function --> hashed_password in db
## password --> hashing function --> hash === hashed_password ???

### Here hash function should be slow
#### 1234mypassword







#=========DAY 2 =================
#Collisions
## How to handle?
## Disallow it?
## Open adressing -> walking through array until find next open slot
    # linear probing (check each)
    # quadradic (check every other)