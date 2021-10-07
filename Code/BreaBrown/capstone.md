## Project Overview
"Treasure Roam"
*My project is a treasure hunt app for fun weekend adventures*
This is an app that people can use to map out their own geocache when they are feeling adventurous. 


**Frameworks used:**
 - materialize, to make everything look real good
 - Mapbox APIs are divided into four distinct services: Maps, Navigation, Search, and Accounts
 

## Data Model

**Models:**
userProfile:
- username
- password

Treasure:
- coordinates
- notes
- placer of treasure(foreign key, user)

<!-- logBook:
- saves username 
- logs date
- treasure(foreign key) 
*extra curricular*
--> 


<!-- 
userExperience:
-input function that allows users to tell their experience -->


## Schedule
(remember rule of always keeping a Minimum Viable Product!)
- week one: set up Django project, user auth system, installing  Map Box API
- week two: vue app that displays the map and coordinates and saves user logs and notes about the geocache
- week three: style with materialize and css