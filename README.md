# White Feather
# Milestone Project 4 - Kelvin Nicholson

![Reptilian Dictionary](/README/mockup.jpg)

This project was done as part of the Code Institute web application development course, this is the final milestone project.

[View live project here](https://mp4-white-feather.herokuapp.com/)
--

---

# Table of Contents

* [UX](#ux)
* [TECHNOLOGIES USED](#technologies-used)
* [TESTING](#testing)
* [DEPLOYMENT](#deployment)
* [CREDITS](#credits)
---

# UX
* ## User Stories
  * First Time User Goals:
    * I want to view all products available.
    * I want to be able to easily understand and navigate the website.
    * I want to View details about individual products.
    * I want to be made aware of how much my purchase is going to cost while browsing.

  * Returning User Goals:
    * I want to be able to recover my password if forgotten.
    * I want to receive confirmation emails.
    * I want to be able to view all my previous orders.

  * Site Owner Goals:
    * I want to be able to add, delete and edit available products.
    * I want the website to clearly indicate it's purpose.
    * I want site visitors to be able to register, login and logout.
    * I want to post blogs and allow registered users to be able to view and comment on these blogs.

* ## Strategy
  * Is to attract new users to the website, and allow them to have an easy and straight-forward shopping experience.

* ## Scope
  * Provide a clean/smooth UX for users.
  * Provide users with the ability to easily browse and find products.
  * Provide users the opportunity to comment on blog posts once registered.

* ## Structure
  * Existing Features:
    * Web pages:
      - Home Page - Users can find a description about the purpose of the website, as well as links to other pages. 
      - Registration Page - Users have the ability to sign up for an account.
      - Login Page - Users have the ability to login to their account.
      - Profile Page - Users can view and edit their delivery information as well as view all past orders. They can also access the blog page from their profile.
      - Blog Pages - Users can view and comment on blogs posted by the site owner.
      - Bag Page - Users can view all items within their shopping bag.
      - Products Page - Users can view all products vailable on the website.
      - Product Details Page - Users can view information about individual items avalable.
      - Product Management Pages - The site owner can edit and/or add products to the store.
      - Checkout Page - Users can securely checkout their items and view what they're paying and what they're paying for.
    * Users will receive a 404 Page if they attempt to direct to a page which does not exist.
    * Navigation: 
      * Users can land on any page of the website and find what they need within 3 clicks.
      * Navigation bar is available on every page and has links to all pages or important functions (login, logout, register).
      * Home page has a search bar to enable users to search the available products.
      * Navabar has individual links to categories of products.
      * Site owner has buttons beneath each product that will allow the user to remove or edit products.
      * The registration, login and logout options will show confirmation to the user.
      * User is redirected to Home Page when clicking on the logo.

  * Future Features:
    * As the comments grow on the blogs and the amount of blogs increases, add pagination to reduce the amount of scrolling to be done when browsing through the blogs and comments.
    * Add the ability to directly contact the store from within the previous orders view.

 * Database

    * Amazon AWS was used to store the data for this website.
      * The model below displays all the fields and their respective data types that are stored within the database.
        ![dbschema](/README/dbschema.png)


     * 8 models are stored in the database.

      * 'Category'
        * Fields stored:
          * name(string)
          * friendly_name(string)

      * 'User'
        * Fields stored:
          * username(string)
          * password(string)

      * 'UserProfile'
        * Fields stored:
          * user (ForeignKey(User))
          * default_phone_number (int)
          * default_street_address1 (string)
          * default_street_address2 (string)
          * default_town_or_city (string)
          * default_county (string)
          * default_postcode (string)
          * default_country (string)

      * 'Product'
        * Fields stored:
          * category (ForeignKey(Category))
          * sku (string)
          * name (string)
          * description (string)
          * has_sizes (boolean field)
          * price (decimal field)
          * image_url (url field)
          * image (image field)

      * 'OrderLineItem'
        * Fields stored:
          * order (ForeignKey(Order))
          * product (ForeignKey(Product))
          * product_size (string)
          * quantity (int)
          * lineitem_total (decimal field)

      * 'Order'
        * Fields stored:
          * order_number (int)
          * user_profile (ForeignKey(UserProfile))
          * full_name (string)
          * email (string)
          * phone_number (int)
          * country (string)
          * postcode (string)
          * town_or_city (string)
          * street_address1 (string)
          * street_address2 (string)
          * county (string)
          * date (date time field)
          * delivery_cost (decimal field)
          * order_total (decimal field)
          * grand_total (decimal field)
          * original_bag (string)
          * stripe_pid (itn)
  

      * 'BlogMod'
        * Fields stored:
          * blog_title (string)
          * blog (string)

      * 'CommentMod'
        * Fields stored:
          * your_name (string)
          * comment_body (string)
          * blog (ForeignKey(BlogMod))

* ## Skeleton
  * Wireframes:
    - [Home](/README/) | [Login](/README/) | [Register](/README/) | [Add Word](/README/) | [Edit Word](/README/) | [Profile](/README/)

  * Sitemap: 
    * All pages navigate to eachother through the use of buttons or the navigation bar.

    ![sitemap](/README/sitemap.png)

  * 404 page:
    * User will be redirected to a 404 error page when attempting to access a page that no longer exists or is unavailable.

* ## Surface 
  * Colour Scheme:

    ![Palette Colours](/README/color-scheme.png)

    * The colours for this project were minimal. Only two colours were used as accents throughout this project. Both are the same colour just varying shades.

    * English Violet - darker shade (45364B)

    * English Violet - lighter shade (62466B)

    * Black (000000) and white (FFFFFF) were used for some text and backgrounds.

  * Typography:
    * 'Lato' font was used throughout the website to keep the text simple and undistracting.

  * Imagery:
    * The background image on the home page and blog page is a buddha statue to represent spirituality based off of the content of the website. This also inspired the purple colour choices throughout the website.

---
* ## Languages
  * [HTML5](https://en.wikipedia.org/wiki/HTML5) - Used to structure the website.
  * [CSS3](https://en.wikipedia.org/wiki/CSS) - Used to style the content of the website.
  * [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Used to create interactivity.

* ## Frameworks, Libraries & Programs
  * [Django](https://www.djangoproject.com/) - Used for authentication, creating templates and url routing.
  * [Amazon AWS](https://aws.amazon.com/) - S3 (Simple Cloud Storage) Used to store the assets of the website.
  * [Heroku](https://www.heroku.com/) - Used for deployment of application.
  * [Bootstrap5](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - Used to make the website responsive, for card panels and for the design of the navigation bar / hamburger menu.
  * [Font Awesome](https://fontawesome.com/) - Used for the icons throughout the website.
  * [Git](https://git-scm.com/) - Used for version control.
  * [GitHub](https://github.com/) - Used to create and host the repository for the website.
  * [Gitpod](https://gitpod.io/) - Integrated Development Environment used to develop the website.
  * [Wirefram.cc](https://wireframe.cc/) - Used for wireframing of the website.
  * [Coolors](https://coolors.co/) - Used to assemble an appropriate colour palette.
  * [Gloo Maps](https://www.gloomaps.com/) - Used to create sitemap.
  * [Powerpoint](https://en.wikipedia.org/wiki/Microsoft_PowerPoint) - Used to create the model for the database schema

---

# Testing
* Please see [TESTING.md](/TESTING.md).

---

# Deployment
This project was deployed to Heroku. This project made use of the Code Institute template which can be found [here](https://github.com/Code-Institute-Org/gitpod-full-template).

## Heroku and Github
1. Once code has been pushed from IDE to Github, go to Heroku.

2. Register/Sign in to Heroku.

3. Create application on Heroku.

4. Select 'Deploy' tab, connect to GitHub under 'Deployment method'.

5. Enable automatic deploys from main branch.

6. You can then make use of deployment link.


## Local Deployment
1. Log in to GitHub and locate this project's [repository](https://github.com/SpooshDoosh/MP4).

2. Select the "Code" dropdown and copy the link provided.

3. You can now paste this link into your IDE terminal.

---

# Credits

* [Smartmockups](https://smartmockups.com/)
* [Code Institute Boutique Ado Project ](https://learn.codeinstitute.net/ci_program/level5diplomainwebappdevelopment)
* [Aleksandar Pasaric](https://www.pexels.com/photo/buddha-statue-during-golden-hour-2070118/)