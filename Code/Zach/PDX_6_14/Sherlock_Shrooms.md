## Project Overview
*This project seeks to create a social-media platform to allow users to post locations and descriptions of mushroom finds utilizing googlemaps!*

**Frameworks used:**
 - Pillow, to display images
 - Materialize, to make everything look real good
 - Googlemaps, to display a map of clues and key locations for the subject
 - Chatsocket (maybe?), to enable users to chat directly

## Functionality

When the user enters the site, if they are authenticated, they will move directly to the home page showing a board of the last 5-10 mushrooms posted to the site. If they are not authenticated, they will be prompted to login or register.

On the home screen, they will also see a map populating with their previously selected favroite mushrooms (they'll be prompted to select these when they make their profile). They'll also be able to message other mushroom scavengers directly on their finds and post their finds which will then also populate on the "master mushroom map" containing everyone's finds.

## Data Model

**Models:**
 - CustomUsers:
	 - fields: profilepic
 - Mushroom Finds:
	 - fields
		 - Species Name
		 - Photo
		 - Location
		 - Soil description
		 - Surrounding plant-life description

## Schedule
- week one: set up Django project, user auth system and user-profiles
- week two: Master mapping features and add chatsocket
- week three: Make it pretty
