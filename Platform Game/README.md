# Platformer

This project is organized using Maven and it is written completely in Java.

The front end of the platform game itself is made entirely using Java Swing. Everything was built from scratch, including game animations and collisison.
It contains the key componenets like a player, a monitoring enemy, platforms, and and end goal of reaching the anchor.  
The backend is built using Java Spring Boot. The backend serves as a RESTful API using Spring MVC and Spring Data to hold information about the different users and their wins and losses. 
The API is split into an Application Class, a Controller, a Model, and a Spring Repository to communicate with the database.

# What I learned
* How to design and implement a large scale project using OOP, complex relationships, and Multithreading
* How to build a user-friendly front end to a game using clean animations, reliable physics, and realistic component collisions
* How to design a RESTful API with java Spring boot using Spring MVC and Spring Data


# Project Organization

- ***Platformer/res/*** contains all the Images needed for the program. 
- ***src/Entities/*** contains code on the platforms, player, moving enemy and the anchor. 
- ***src/Levels/*** contains the level information with the platform placement 
- ***src/Physics/*** contain one of the most key parts which is the collision detection system which we made
- ***src/gamestates/*** contains code on what to do in different parts of the game like pause, setting, playing and game over
- ***src/inputs/*** contains all the listeners like mouse and keyboard listener
- ***src/main/*** contains the foundation code like the main method, game panel and window which will actually display the running code
- ***src/utilz/*** contains the constants like the length of the animation rows and the directions as well as a load save method which will load in all the information at the start
