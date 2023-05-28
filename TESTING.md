# Testing

# Browser Compatibility
---
This website has been tested and operates as expected on Chrome, Microsoft Edge, Safari, Firefox and Opera browsers.

The website has been tested using Chrome Devloper Tools for it's responsiveness on various device viewports.

It responds as intended on the following devices:

* iPhone XR 

* iPhone 12 Pro

* Pixel 5

* Samsung Galaxy S20 Ultra

I personally tested the website on my Google Pixel 7 Pro.

# User Stories Testing

* First Time User
    * I want to view all products available.
        * On the homepage there is a button below the welcome message that will take the user to the products page, or they can make use of the links on the navbar.

        ![ft1](/TESTING/ft1.png)

        ![ft1.5](/TESTING/ft1.5.png)

    * I want to be able to easily understand and navigate the website.
        * There is a navigation bar along the top of every page. The navigation bar is permanently fixed to the top of the screen and is always visible. Clicking on the logo will return the user to the homepage. There are buttons throughout the website with a clear description of their purpose.

        ![ft2](/TESTING/ft2.png)

        ![ft2.5](/TESTING/ft2.5.png)

    * I want to View details about individual products.
        * Each product has an individual page detailing information about the product. There is also a quantity selector and a button to add it to the shopping bag.

        ![ft3](/TESTING/ft3.png)

        ![ft3.5](/TESTING/ft3.5.png)

     * I want to be made aware of how much my purchase is going to cost while browsing.
        * When an item is added to the shopping bag, the total is updated on the navbar, so that as the user browses their total is always visible.

        ![ft4](/TESTING/ft4.png)

* Returning User
    * I want to be able to recover my password if forgotten.
        * There is a password recovery page for user that have previously registered on the site, this is located on the log in page.

        ![ru1](/TESTING/ru1.png)

    * I want to receive confirmation emails.
        * Upon registering, users will need to authenticate the registration which they can do by clicking the link on the email confirmation sent to their email.

    * I want to be able to register and/or login.
        * The login and registration links are found within the navigation bar - account dropdown button.

        ![ru2](/TESTING/ru2.png)

    * I want to be able to view all my previous orders.
        * Once registered and looged in. If a user has made a previous order they can localte this via their individual profile.

        ![ru3](/TESTING/ru3.png)

* Site Owner
    * I want to be able to add, delete and edit available products.
        * Once logged in as a superuser, buttons beneath each product will appear (edit and delete). The superuser will also have access to a product management page to add products to the site.

        ![so1]()

    * I want the website to clearly indicate it's purpose
        * On the home page there is a brief explanation of what the site is for.

        ![so2](/TESTING/)

    * I want site visitors to be able to register, login and logout.
        * The site has register, loging and logout functionality. These links can be found on the navbar upon clicking on the account dropdown button.

        ![so3](/TESTING/so3.png)

        ![so3.5](/TESTING/ft3.5.png)

    * I want to post blogs and allow registered users to be able to view and comment on these blogs
        * Superusers can add blog post via the admin panel once logged in. Site users can view these posts as well as leave comments on them, as long as they are registered.

        ![so4](/TESTING/so4.png)

        ![so5](/TESTING/so5.png)

---

# Code Validation

## HTML

Each page of the website was run through the W3C Markup Validation Service to ensure there were no errors. Could not succesfully run the tests due to errors being thrown from the Jinja templating syntax ({% for %} {% endfor %} etc).

## CSS

The website's CSS was run through the W3C CSS Validation Service (Jigsaw). No issues or errors were found.

* base.css
    ![css](/TESTING/css-base.png)

* checkout.css
    ![checkoutcss](/TESTING/css-checkout.png)

* profile.css
    ![profilecss](/TESTING/css-profile.png)
---

# Lighthouse

Tests on Lighthouse were decent, however there were some performance issues due to images being served could be compressed and served in next-gen formats.
---

# Debugging

## Resolved

* Initially I was having issues requiring me to reinstall all packages everytime I ran the workspace.
    * Did not realise I was running multiple workspaces each time I went to work on the project.

* 'OrderForm' object has no attribute 'get'
    * After uninstalling and reinstalling all packages, downgrading and upgrading packages and countless hours with tutor assistance, the issue was located. I had made use of 'super().__init__(self, *args, **kwargs)' which did not require 'self'. After this issue was corrected. I recieved an additional error but the solution was the same - to remove 'self'.

## Unresolved

* All images need to be compressed and served in a next-gen format (such as webp).