
# Election Platform - South Africa Elections

## Overview

This is my first Django application where I’ve integrated Firebase Firestore to create an election platform for South African elections. The platform allows users to register, log in, view party manifestos, and cast votes. The app also provides real-time polling results, displaying the current percentage of votes for each party.

Although I couldn't complete all the features due to time constraints, the app demonstrates the main functionalities, including user registration, login, and the viewing of party manifestos with a pop-up feature.

## Features

- **User Registration**: Users can create an account by providing their username, email, and password. Disposable emails are flagged using the UserCheck AI API to ensure valid email addresses.
- **Login**: Registered users can log in by entering their email and password. The app checks the credentials against Firebase Firestore.
- **Manifesto Viewing**: Users can view a party's manifesto, which is fetched from the Firebase Firestore database and displayed in a pop-up.
- **Voting (Not Finished)**: The app includes a vote functionality where users can cast their votes. The voting section and live polling results weren't fully completed, but the voting logic has been implemented in the backend.
- **Real-time Polling Results (Not Finished)**: Displays the percentage of votes for each party, but this feature isn’t fully functional as of now.

## Technologies Used

- **Django**: Backend framework used for building the web application.
- **Firebase Firestore**: NoSQL database used for storing user data, manifesto data, and voting results.
- **Tailwind CSS**: A utility-first CSS framework for styling the application.
- **jQuery**: For handling AJAX requests to fetch and display the manifestos.
- **UserCheck AI API**: Used to validate email addresses during registration, flagging disposable emails.

## Challenges

This project marked my first time working with Django and Firebase Admin SDK, and it was quite a challenge to integrate everything smoothly. While the app demonstrates the primary logic for registration, login, manifesto viewing, and voting, I was unable to complete the live polling results and voting functionality entirely. Nevertheless, the app provides the foundation and shows how it can be expanded in the future.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/election-platform.git
cd election-platform
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Firebase Setup

1. Go to the [Firebase Console](https://console.firebase.google.com/).
2. Create a new project and enable Firestore.
3. Download the **service account key** from Firebase and place it in the root directory of the project.
4. Update `settings.py` with the path to your Firebase service account key:

```python
FIREBASE_CREDENTIALS = BASE_DIR / "firebase-adminsdk.json"  # Path to your service account JSON file
```

### 4. Configure Django Settings

Ensure the settings for Firebase, session management, and URLs are set up correctly in `settings.py`.

### 5. Migrate the Database

Although Firebase Firestore is used to store data, Django may still require some migrations for other functionalities. Run the following command to apply migrations:

```bash
python manage.py migrate
```

### 6. Run the Development Server

To run the Django development server locally:

```bash
python manage.py runserver
```

### 7. Access the Application

Navigate to `http://127.0.0.1:8000` in your browser. You can:

- **Register** a new account.
- **Log in** with an existing account.
- **Vote** for a party (functionality not fully implemented).
- **View Manifestos** of each party.
- See the **real-time polling results** (incomplete).

## Structure of the App

### 1. **URLs**

- `/register/`: The registration page where users can sign up.
- `/login/`: The login page where users can log in to the platform.
- `/voter-portal/`: The main page for logged-in users where they can vote and view polling results.
- `/logout/`: Logs the user out and redirects to the login page.

### 2. **Views**

- **Registration View**: Handles user registration and form validation.
- **Login View**: Authenticates the user by comparing the entered credentials with Firestore data.
- **Voter Portal View**: Displays the voting options, manifesto view, and allows voting.
- **Logout View**: Logs out the user and redirects to the login page.

### 3. **Database** (Firestore)

- **`voters`**: Stores user data (username, email, password).
- **`results`**: Stores voting data for each party (email of the user, party voted).
- **`manifestos`**: Stores the manifesto data for each party.

## Running the Project on Windows

To run the project on Windows:

1. Open a terminal or command prompt.
2. Navigate to the project folder.
3. Run the command:

```bash
python manage.py runserver
```

4. Access the app in your browser at `http://127.0.0.1:8000`.




