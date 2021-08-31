## Project Overview
*My project is super duper great and shows videos of robots that make pie*
The problem this project solves is that people have never seen robots make pie before. 
**Frameworks used:**
 - pillow, to display images
 - materialize, to make everything look real good
 - robotsRus, an API that has everything robot related and EXCELLENT documentation
 
## Data Model

**Models:**
 - CustomUsers:
	 - fields: profilepic
 - Robots:
	 - fields
		 - Name (charfield)
		 - description( charfield)
		 - owner (foreignkey to user)

## Schedule
(remember rule of always keeping a Minimum Viable Product!)
- week one: set up Django project, user auth system, and API of all robots making pie 
- week two: vue app that displays robots and saves to user fav lists on API 
- week three: Make it look reall really good
