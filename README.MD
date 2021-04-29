
Hello!

The functionality of this application is developed using:
    
1. Django Rest Framework ( For creatingRESTful API)
2. Djoser (To simplify the work with the user profile)
3. AmazonS3 (For storing user pictures)

Installing and testing on a local machine:
1. Clone the repository with git clone.
2.Create core/local_settings.pyand write the DB settings, Amazon S3 and token.
3. Apply migrations by typing in terminal python manage.py migrate.
4. Enter into terminal python manage.py runserver.
5. Create a user and login with Djoser.

Endpoints:
1. Portfolios
    1. [GET] portfolios/  - To view your portfolios
    2. [POST] portfolios/create  - To create a new portfolio
    3. [PATCH] portfolios/<int:pk>/update  - To edit a portfolio
    4. [DELETE] portfolios/<int:pk>/delete  - To delete a portfolio
2. Images
    1. [GET] images/  - To view and search images
    2. [POST] images/create  - To create a new image
    3. [PATCH] images/<int:pk>/update  - To edit an image
    4. [DELETE] pimages/<int:pk>/delete  - To delete an image

3. Comments
    1. [POST] images/<int:image_id>/comments/create - To create a comment below the image

Djoser docs with endpoints: https://djoser.readthedocs.io/en/latest/getting_started.html

Deployed heroku app: https://cryptic-bastion-26002.herokuapp.com/
