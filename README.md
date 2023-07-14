# ToDoApp
A Django based basic backend for a basic to do app 

# Endpoints

# 1. /api/todo/

     1. for Admin
        GET : List all todo tasks with user id
        POST : Post a new task and associate it with a user
        
     3. for User
        GET : List all task created by the user
        POST : Creates a new task for the user

# 2. /api/todo/{id}/
     for updating/ deleting the task
     (Note : Admin can change user/task for all user but regular user can change task associated with him only)

# 3. /auth/users/
    creates and lists all users to admin

# 4. /auth/users/me/
    for getting/updating details of current user

# 5. /jwt/create/
    for JWT getting access and refresh token
    
# 6. /auth/jwt/refresh/
    for getting new access token



Note: Authentication/user endpoints are implemented using djoser




        
        
