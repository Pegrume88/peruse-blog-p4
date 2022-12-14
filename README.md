# Peruse

Peruse is a blog app that alows users to create a profile and post as well as view other posts from the community. The users can intereact with each other through liking posts and posting comments.

Each user has the choice to create profile and make it as indepth and interesting as they would like.

![ReadME Image](/static/image/readme-image.png)

# USer Experience

## User stories

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### As an unregistered, I want to :

* View Posts
* View Posts by categories



### As a registered user, I want to:

* As a user i want to be able to sign up 
* As a user i want to be able to Login 
* As a user i want to be able to Create a profile 
* As a user i want to be able to add Posts 
* As a user i want to be able to View Posts  
* As a user i want to be able to like and comment  
* As a user i want to be able to View Posts by categories 
* As a user i want to be able to add new categories 
* As a user i want to be able to delete Posts 
* As a user i want to be able to edit Posts 
* As a user i want to be able to edit account settings
* As a user i want to be able to add social media links to my profile and posts




### As a registered admin, I want to:

* As the admin I want to be able delete Users Account 
* As the admin I want to be able delete Users Posts 
* As the admin I want to be able delete User comments 
* As the admin I want to be able delete User Profiles 

# Design

### Overall feel
The overall feel I want to give to this application is a clean simple design
## Wireframes and Initial Design
This were my innitial design ideas. There are some changes due to authorised users 
having a slightly defferent view to un authorised users:

![wireframes](/static/image/Peruse.png)
![wireframes](/static/image/mobile_design.png)

# Features

## Current Features

### Navigation menu displayed across all pages

The navigation menu is displayed on all pages. and is when viewed
on a mobile device the nav bar links colapse in a dropdown menue.
The nav bar will display different options depending on where a user
is logged in or not.

### User acount registration

This page allows users to register with the application to view 
all the options available for authorised users.

### User create Profile 

This allows the user to create a profile, they can add a profile picture
as well as a bio and links to thier social media

### Crud Functionality
 the user can add create, delete and edit their posts as well as view all posts.
 the admin can read, add, delete and edit a users profile, account setting, posts and comments.

### Possible Future Features

A possible feature could be to allow useres to view a post with the most likes
to follow which posts are trending. 
Another feature could be for the suer to choose a selections of categories in which they are interested, allowing their feed to only show categores the user wants to see.

### Defensive Design Features

The defensive features that I have added revolve around if a user has regestered,
If you the user is logged in then they can add posts, comment, and like posts. As well creating a profile page and edit their account setting.

Users can only edit and delete their own posts.


### Categories

Users can view posts under a specific category via a dropdown menu located
in the nav bar. 

If the user is logged in they will be able to add their own categories.

# Testing

### Manual testing
I manually went through the application and it features to manually test all links and pages.
All links and pages run correctly and there were know errors diplayed.

### Automated testing
Due to time constraints I was only able to create one automated test.
I tested the validation of the post form. And the form ws validated.

# Validators

## HTML

* category view - Html passed validition, a few erros raised due to the django elements

* Add category - Html passed validition, a few erros raised due to the django elements

* Base template - Html passed validition, a few erros raised due to the django elements

* add post - Html passed validition, a few erros raised due to the django elements

* edit post - Html passed validition, a few erros raised due to the django elements

* Delete Post - Html passed validition, a few erros raised due to the django elements

* Index page - Html passed validition, a few erros raised due to the django elements

* create user Profile - Html passed validition, a few erros raised due to the django elements

* Edit profile - Html passed validition, a few erros raised due to the django elements

* User Profile - Html passed validition, a few erros raised due to the django elements

* Edit Account - Html passed validition, a few erros raised due to the django elements

* Signup page - Html passed validition, a few erros raised due to the django elements

* Login in page - Html passed validition, a few erros raised due to the django elements

## Python

I ran all python files through PEP8 to validate the files. 
The errors that were found were mostly about line length.


## CSS

I rand all css through the WS3 css validator with no Errors

## Javascript

I only used A couple of lines of JS in my application to allow fors to grab the correct user information.

I ran the JS through JShint with errors.

## LightHouse

![LightHouse](/static/image/lighthouse.png)

The light house test didnt show the best results for porformance. In fact it was extremely poor. I tried to improve the result but i didnt see much of an improvement. With more time i possibly could get this score up to a respectable level.

There rest of the scores are respectable but but other than best practices they could all be improved.

# Technologies Used

### FrameWorks

* Django

* Bootstrap

### languages

* Python
* HTML
* CSS
* JavaScript


### Others

+ [render](https://dashboard.render.com/) used to deploy live site.
+ [GitHub](https://github.com/) used to host repository.
+ [GitPod](https://www.gitpod.io/) used to develop project and organise version control.
+ [Canva](https://www.canva.com/) used for the inital design. 
+ [RandomKeygen](https://randomkeygen.com/) used to create a strong password for required  `<SECRET_KEY>`.
+ [Lighthouse](https://developers.google.com/web/tools/lighthouse) for performance review.
+ [Am I Responsive](http://ami.responsivedesign.is/) used to generate README intro image.

## Deployment

I used Render to deploy my code due to the changes With Heroku which lead with me being unable to register. 

Rander makes it really easy to Deply. Once you connect your GitHub or GitLab account to your Render account, Render will automatically build and deploy your services with every push. For more information on connecting your Git accounts to Render, see our docs for GitHub and GitLab.

### Connecting GitHub

When you create your first service on Render you will have the option to connect GitHub.

Clicking on Connect GitHub will redirect you to github.com where you can authorize Render to access your repositories. You will then be redirected back to Render where you will see a list of your GitHub repos. You can then proceed by clicking on the repo you’d like to use for your service.







