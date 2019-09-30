# TodoApp_Api
A simple to-do list application with Django using the API approach.

---

# Instructions to test the App
1. Steps to run server
  - clone the repository from github
  - migrate to the todo app folder
  - create a virtual environment by runing 'py -m venv env'
  - activate the virtual environment using '.\env\Scripts\activate
  - install django on the virtual environment using  'pip install django'
  - run 'python manage.py runserver' to run the server
  - copy address to a browser
  
2. Steps to access the site admin
  - place the ip address:  http://127.0.0.1:8000/admin on the browser to access the admin site
  - Use 'isaac' as username and 'walice' as password
  - from the admin you can access the model
  
3. Steps to access the api 
  - place the ip address:  http://127.0.0.1:8000/todos on the browser to access the todos in Json format
  - place the ip address:  http://127.0.0.1:8000/id to access each todos
  - Note: id can be 1, 2 or 3.
