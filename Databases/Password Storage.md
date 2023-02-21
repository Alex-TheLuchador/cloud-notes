# Storing Passwords in a Database

Plain-text password storage is an awful practice, and understanding how to properly store passwords in a database is critical to keeping a system safe in the event of an intrusion.

## Hashing

Putting your plain-text passwords through a modern hashing algorithm produces a secure string of text. Hashes are one-way functions, meaning they cannot be decrypted.

However, it is possible to have two different inputs produce the same hashed output (a common strategy used in pre-computation attacks), and so we can add other measures like Salting.

## Salting

Salts are unique and random strings that are appended to passwords to further randomize the hashing process. A password is combined with a salt to produce a hash, so the process looks like this:

password + salt = hash

fidoTheDOG89% + seasons = a89sd7f6a890sd7f6809a7sdf690a8sdfty907d

The random string produced in our example is much different that the hash that would have been generated if we passed in the password by itself, without the salt. This is how salting can increase the safety of your password storage.

## Storage and Authentication

Passwords can be stored in a database by having the salt occupy one column and the hash occupy the other. The password is NOT stored on the database.

1. The user enters their password at login.
2. The database takes that entered password and adds the salt to it.
3. The combination formed in the previous step is put through a hashing algorithm.
4. A check is run to compare the hash from the previous step with the hash stored in the database. If the hashes are the same, then that means the user entered the correct password.