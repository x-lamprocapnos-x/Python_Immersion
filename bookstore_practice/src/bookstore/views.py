from django.shortcuts import render, redirect
# Django authenticaiton libraries
from django.contrib.auth import authenticate, login, logout
# Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm

# Define a function based view called login_view that takes a request from a user
def login_view(request):
    #error_message to None
    error_message = None
    #Form object with username and password fields
    form = AuthenticationForm()


    # When user hits "login" button, then POST request is generated
    if request.method == 'POST':
        # Read the data sent by the form vis POST request
        form = AuthenticationForm(data=request.POST)

        # Check if form is valid
        if form.is_valid():
            username = form.cleaned_data.get('username')# Read username
            
            password = form.cleaned_data.get('password')# Read password

            # Use Django athenticate function to validate the user
            user = authenticate(username=username, password=password)
            if user is not None: # If user is authenticated

            # Then use pre-defined Django function to login
                login(request, user)
                return redirect('sales:records') # & send the user to desired page

        else:
            # In case of error, print error message
            error_message = 'Ooops.. something went wrong'
    
    # Prepate data to send from view to template
    context ={
        'form': form, # Send the form data
        'error_message': error_message # & the error message
    }
    # Load the login page using 'context information
    return render(request, 'auth/login.html')

# Define a function based view called logout_view that takes a request from the user
def logout_view(request):
    # The use pre-defined Django function to logout
    logout(request) 
    # after logging out go to login form (or whichever page you desire)
    return redirect('login')





