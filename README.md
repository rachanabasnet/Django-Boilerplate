# Django Boilerplate

## STEPS TO GET STARTED

### `Create virtual environment`

- #### 1. Install virtual environment
  ```
  pip install virtualenv
  ```
- #### 2. Create virtual environment (create virtual env outside the django project)
  ```
  virtualenv <virtual_env_name>
  ```

### `Install project requirements`

- #### Install requirements.txt file packages
  ```
  pip install -r requirements.txt
  ```

### `Migrate Table`

- #### Migrate all tables to database using a command below:
  ```
  python manage.py migrate
  ```

### `Create super user`

- #### create superuser for the project.
  ```
  python manage.py createsuperuser
  ```

### `Run server`

- #### Run the django server.
  ```
  python manage.py runserver
  ```
