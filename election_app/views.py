import firebase_admin
from firebase_admin import auth, firestore, credentials
from django.shortcuts import render, redirect
from django.contrib import messages
from election_platform.settings import FIRESTORE_DB  # Firestore database reference
from .forms import RegistrationForm
import requests
import http.client
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


# Index page (home page)
def index(request):
    return render(request, 'index.html')

# UserCheck API Key for email validation
USERCHECK_API_KEY = 'yY3jT6rL5KdBbUswsO6NtDQsNYbCEXjb'  # API key for UserCheck

# Registration view
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # Extract form data
            username = form.cleaned_data.get('username', '').strip()
            email = form.cleaned_data.get('email', '').strip()
            password = form.cleaned_data.get('password', '').strip()
            repeat_password = form.cleaned_data.get('repeat_password', '').strip()
            id_number = form.cleaned_data.get('id_number', '').strip()  # Remove leading/trailing spaces
            phone_number = form.cleaned_data.get('cellphone_number', '').strip()
            confirm_phone = form.cleaned_data.get('confirm_cellphone_number', '').strip()


            # Check if passwords match
            if password != repeat_password:
                messages.error(request, 'Passwords do not match!')
                return render(request, 'registration/register.html', {'form': form})

            # Validate email with UserCheck API
            try:
                if not validate_email(email):
                    messages.error(request, 'Disposable email addresses are not allowed. Please use a valid email address.')
                    return render(request, 'registration/register.html', {'form': form})
            except Exception as e:
                messages.error(request, 'An error occurred during email validation. Please try again.')
                print(f"Email validation error: {e}")
                return render(request, 'registration/register.html', {'form': form})

            # Check if email already exists in Firestore
            try:
                existing_voter = FIRESTORE_DB.collection('voters').where('email', '==', email).get()
                if existing_voter:
                    messages.error(request, 'A voter account is already registered with this email address.')
                    return render(request, 'registration/register.html', {'form': form})
            except Exception as e:
                messages.error(request, 'An error occurred while checking existing accounts. Please try again.')
                print(f"Firestore query error: {e}")
                return render(request, 'registration/register.html', {'form': form})

            # Store user data in Firestore
            try:
                FIRESTORE_DB.collection('voters').add({
                    'username': username,
                    'email': email,
                    'password': password  # Warning: Password should ideally be hashed!
                })
                messages.success(request, 'Registration successful! You are now registered to vote.')
                return redirect('login')
            except Exception as e:
                messages.error(request, 'Registration failed. Please try again later.')
                print(f"Error storing data in Firestore: {e}")
                return render(request, 'registration/register.html', {'form': form})
        else:
            messages.error(request, 'Form submission is invalid. Please correct the errors and try again.')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})



# Email validation using UserCheck API
def validate_email(email):
    """
    This function checks if the email is disposable using the UserCheck API.
    """
    try:
        response = requests.get(
            f'https://api.usercheck.com/email/{email}',
            headers={'Authorization': f'Bearer {USERCHECK_API_KEY}'}
        )
        
        # Ensure a valid response was received
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code} from UserCheck.")
            return False

        data = response.json()

        # Check if the email is disposable
        return not data.get('disposable', False)  # True if not disposable, False otherwise

    except Exception as e:
        print(f"Error validating email: {e}")
        raise  # Rethrow the exception to handle in the calling function


db = firestore.client()
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Query Firestore for the user by email
            user_ref = db.collection('voters').where('email', '==', email).limit(1).get()

            # Check if any user document was found
            if not user_ref:
                messages.error(request, "No account found with this email address. Please register first.")
                return render(request, 'login.html')

            # Retrieve the user document
            user = user_ref[0].to_dict()

            # Check if the provided password matches the stored password
            if password == user['password']:  # Simplified password check
                # Store session data with the logged-in user's details
                request.session['username'] = user['username']  # Store the username in session
                request.session['email'] = user['email']
                request.session['uid'] = user_ref[0].id  # Using Firestore document ID as UID

                # Successful login, redirect to the voter portal page
                return redirect('voter_portal')  # Redirect to the voter portal page

            else:
                messages.error(request, "Incorrect password. Please try again.")
                return render(request, 'login.html')

        except Exception as e:
            messages.error(request, "An error occurred while logging in. Please try again.")
            print(f"Login error: {e}")
            return render(request, 'login.html')

    return render(request, 'login.html')

# Logout view
def logout_user(request):
    # Clear the user session
    request.session.flush()  # This clears all session data
    
    # Redirect to the login page without showing any success message
    return redirect('login')

    
# Dashboard view
def dashboard(request):
    # Simulated example for dynamic data; replace with actual queries to Firestore
    candidates = [
        {"name": "Party A", "leader": "John Carter", "slogan": "Unity for Progress", "manifesto": "Advancing education."},
        {"name": "Party B", "leader": "Sarah Johnson", "slogan": "Equality for All", "manifesto": "Economic stability."},
        {"name": "Party C", "leader": "Emily Brown", "slogan": "Innovation for Tomorrow", "manifesto": "Empowering youth."}
    ]

    total_votes = 1200  # Example total votes
    population_voted = (total_votes / 100) * 100  # Example population size of 100

    return render(request, 'dashboard.html', {
        "username": request.session.get("username", "Voter"),
        "candidates": candidates,
        "total_votes": total_votes,
        "population_voted": population_voted,
    })


db = firestore.client()

# AJAX view to fetch manifesto data for a specific party
def get_manifesto(request):
    party_name = request.GET.get('party_name')

    try:
        # Fetch manifesto data for the selected party from Firestore
        party_ref = db.collection('manifestos').document(party_name)
        doc = party_ref.get()

        if doc.exists:
            manifesto_data = doc.to_dict()
            leader = manifesto_data.get('leader')
            slogan = manifesto_data.get('slogan')
            manifesto = manifesto_data.get('manifesto')

            # Return data as JSON response
            return JsonResponse({
                'success': True,
                'party_name': party_name,
                'leader': leader,
                'slogan': slogan,
                'manifesto': manifesto
            })
        else:
            return JsonResponse({'success': False, 'message': 'Manifesto not found.'})

    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({'success': False, 'message': 'An error occurred while fetching the manifesto.'})
    
def voter_portal(request):
    # This function is called when a user visits the '/voter-portal/' page.
    # You can return data like polling results, or show the user their voting status.
    return render(request, 'voter_portal.html')