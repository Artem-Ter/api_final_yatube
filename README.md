# Platform for publishing posts and comments on them with API.

## Project description:

Platform for publishing posts and comments. It is possible to: create groups, make posts, subscribe to authors.

The project created using HTML temlates.
For authentication JWT tokens are used.
Restriction and roles:
- view contect - everyone
- create content - authenticated users
- change content - content's author

## How to launch a project:

Clone the repository and switch to it using the command line:
```
git clone git@github.com:Artem-Ter/api_final_yatube.git

```
```
cd api_final_yatube
```
Create and activate virtual environment:
```
python3 -m venv env
```
```
source env/bin/activate
```
```
python3 -m pip install --upgrade pip
```

Install dependencies from a file requirements.txt:
```
pip install -r requirements.txt
```

Make migrations:
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```

Run project:
```
python3 manage.py runserver
```

## Technologies used:

- Python;
- Django Framework;
- Django-Rest-Framework;
- JWT;
- Djoser;

## Endpoints API Yatube:

- (GET, POST): get a list of all posts or create a new post.
```
api/v1/posts/
```
- (GET, PUT, PATCH, DELETE): get, edit or delete a post by id.
```
api/v1/posts/{post_id}/ 
```
- (GET): get a list of all groups.
```
api/v1/groups/ 
```
- (GET): get information about a group by id.
```
api/v1/groups/{group_id}/ 
```
- (GET, POST): get a list of all post comments with id=post_id or create a new one by specifying the id of the post we want to comment on.
```
api/v1/posts/{post_id}/comments/ 
```
 - (GET, PUT, PATCH, DELETE): get, edit or delete a comment by id for a post with id=post_id.
```
api/v1/posts/{post_id}/comments/{comment_id}/ 
```
- (GET, POST): get a list of all subscriptions or create a new subscription.
```
api/v1/follow/ 
```
- (POST): we pass the login and password, we get the token.
``` 
api/v1/jwt/create/ 
```
- (POST): pass a refresh token, get a new access token.
```
api/v1/jwt/refresh/ 
```
- (POST): verifying the token.
```
api/v1/jwt/verify/ 
```
In response to POST, PUT, and PATCH requests, the API returns the object that was added or changed.


## Project author
[Artem Tereschenko](https://github.com/Artem-Ter)
