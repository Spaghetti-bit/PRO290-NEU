# PRO290-NEU
Project for PRO290-S2 Spring 2024 Q2


Design Document – PRO290 Spring 2024 – Q2
E-Commerce Site										
Team:
Byron Quirk
Christian Vaughn
Execute Summary:

A simple, light-weight website used to order various models of summertime fun! Super soakers and other fun doo-dads would be available on the site for registered users to order. 


Technical Summary:

It’ll use a combination of Mongo and Redis for the backend databases for a quick, responsive, and seamless experience. We’ll be using Docker to containerize and distribute our website. Ocelot will be our gateway with eureka being our registry service.

Targeted Userbase:

Parents that are looking to get toys and to distract their children during the summertime. Especially in the warmer regions of the US.


 
Business requirements for the PRO290 class Service-Based Architecture.

3 Microservices:
	Order Service
-	Handles orders and sends emails through a 3rd party to the user.
-	Order Model
	User Service
-	Login/Create Account/Token auth. (Email set up)
-	MongoDB
-	User Model
	Basket / Cart Service (tied to login)
-	Token authentication. (From the User service)
-	Redis
Language: C#, Docker
Testing Method: Postman
Front-End: Springboot, Bootstrap (for CSS styling)
Stretch-Goals:
-	Online distribution, AWS. Actually hosting it online.


 
Week By Week (SCRUM):
Week 1: Design document, basic schematic of the overall project. Research of any technologies used in the project.
Week 2: Set up the databases (MongoDB, Redis). Basic web structure for front-end
Week 3: Back-End, extensive testing of end-points to make sure the services can be implemented.
Week 4: Implementation, Check up. Final checks for the project. Making sure that it can be deployed locally via docker.
Week 5: Possible stretch goals. Online deployment.


