# Election Platform - South Africa Elections

## Project Rationale

This project represents my first deep dive into using **Django** as a web framework and **Firebase Firestore** as a NoSQL database backend. My goal was to build a fully functional election platform where users could register, log in, view party manifestos, and vote in a simulated election environment. 

While some features are still under development, the platform demonstrates the core functionalities needed for a voting system, showcasing my learning journey and the challenges I faced while working with Django and Firebase for the first time.

## Project Overview

The Election Platform is designed to simulate a voting process for South African elections. Here's what the application currently achieves:

- **User Registration**: Users can register by creating an account, with email validation using UserCheck AI to ensure no disposable emails are used.
- **User Login**: Registered users can log in by entering their email and password, which are verified against stored data in Firebase Firestore.
- **View Party Manifestos**: Users can view detailed manifestos for each political party. These manifestos are stored in Firestore and fetched dynamically, displaying them in a pop-up.
- **Voting Feature**: The voting functionality allows users to vote once for their preferred party. The vote is recorded in Firestore, preventing duplicate voting. The real-time polling percentage is designed to show the party standings based on a total population of 100 voters.
- **Real-time Polling Results (Work in Progress)**: Although I was unable to fully implement the polling results, the logic for counting votes is in place, and data can be retrieved from Firestore.

## Technologies Used

- **Django**: Backend web framework for handling routes, views, and server logic.
- **Firebase Firestore**: NoSQL database for storing user data, party information, manifestos, and voting records.
- **Tailwind CSS**: A utility-first CSS framework for quick and clean styling.
- **jQuery**: For making AJAX requests to fetch and display manifestos in a pop-up.
- **UserCheck AI API**: Used to validate email addresses during registration, preventing disposable emails.

## My Approach

### 1. **User Registration**
   - I implemented a registration form using Django’s form handling system.
   - For email validation, I integrated the UserCheck AI API to prevent disposable email addresses. This ensures that registered users provide legitimate emails.
   - Data is stored in Firestore, including the user's username, email, and password. Although the current setup does not hash passwords (this was a conscious decision due to the learning curve), it allows for future security improvements.

### 2. **Login**
   - Users can log in with their registered email and password.
   - During login, I made sure the credentials are checked against data stored in Firestore. The app checks if the user exists and if the password matches.
   - I chose to utilize Django’s session management to maintain user login state without displaying any login success page—directly redirecting users to the voter portal.

### 3. **Viewing Manifestos**
   - Each political party’s manifesto is stored in Firestore, allowing the app to dynamically fetch and display data.
   - I chose to use a pop-up modal to present the manifesto content. The pop-up takes up 60% of the screen height, allowing users to scroll and view the complete content.

### 4. **Voting Logic (Incomplete)**
   - While the voting logic is partially implemented, users can cast a vote, which is stored in Firestore.
   - The intention was to implement a system that restricts voting to once per user, with the app providing feedback if the user attempts to vote again.
   - I planned to display the voting results in real-time, showing each party’s percentage of the total votes based on a population of 100. Due to time constraints, this feature remains incomplete.

## Challenges and Learnings

This project was my first attempt at building a full-stack web application with Django and Firebase Firestore. Here are some of the challenges I faced:

- **Learning Django**: I started with no prior experience, so understanding Django’s routing, view handling, and template system took some time. However, it gave me insight into how a powerful backend framework operates.
- **Integrating Firebase Firestore**: Using Firebase’s Firestore with Python was challenging, especially figuring out how to perform queries and data operations. It was my first time working with Firebase Admin SDK, and I learned a lot about how NoSQL databases function.
- **User Authentication**: Managing user sessions and ensuring secure login operations was complex, especially since I wanted to avoid displaying explicit success/failure pages after login.
- **Polling Results**: Although I started implementing the voting system, integrating live updates and calculating percentages accurately based on a fixed population proved to be challenging.
- **Handling Errors**: Debugging API calls and integrating external services like UserCheck AI was an experience in patience and persistence.

## Project Setup




To clone my repo: https://github.com/hecreatescoding/Election-app


To run the development server locally:

```bash
python manage.py runserver
```

###. **Access the App**

Navigate to `http://127.0.0.1:8000` in your browser to access the homepage.

## How to Use the App

- **Register**: Go to the registration page, fill in the form, and submit to create an account.
- **Log in**: Use your registered email and password to access the Voter Portal.
- **View Manifestos**: Click on "View Manifesto" for any party to read their policies in a pop-up window.
- **Vote**: The voting functionality is partially complete, allowing you to vote for a party. You will receive a notification if you've already voted.

## Future Enhancements

- **Complete Voting System**: Implement a full voting system that restricts duplicate voting and displays real-time polling updates.
- **Improved Security**: Implement password hashing and email verification for better security.
- **Enhanced UI**: Add more dynamic features, including real-time chart updates for polling results.
- **Deployment**: Move the app from a local environment to a cloud-hosted environment for broader access.



## Acknowledgements

I want to thank everyone who has supported me through this project. This was my first time working with Django and Firebase, and despite the challenges, it was a valuable learning experience!






