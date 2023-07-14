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

# 3. /jwt/create/
    for creating user

# 4. /auth/jwt/verify/
    for getting JWT access and refresh token
    
# 5. /auth/jwt/refresh/
    for getting new access token

# 6. /auth/users/
    lists all users to admin
    
# 7. /auth/me/
    for getting and updating details of current user


Note: Authentication/user endpoints are implemented using djoser




        
        
