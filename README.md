run server python3 spelling_server.py
run client python3 spelling_client.py

Design Pattern Implementation

Singleton pattern.

We can see the singleton pattern implemented for the client class.
The init method of the class sets the __instance to itself when the first object is created.

After that if we wanted to create another object that referenced the previously created one we would use
the getInstance() method which would, if it existed, return the instance of the previously created object and
if other instances didn't exist it would initialize a new object.

We can see that proven in the print 