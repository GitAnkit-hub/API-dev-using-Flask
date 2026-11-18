# IPL Data Analysis – Building APIs Using Flask

Hi everyone!

I have been exploring the concept of **API development**, understanding how APIs work and how widely they can be used to make data and functionality accessible to others.

## What are APIs?

An **API (Application Programming Interface)** is a way for different software applications to communicate with each other.

In our case, we use Flask to expose Python functions and their underlying logic through URLs (API endpoints). When someone sends a request to these endpoints with the appropriate inputs, the server processes the request and returns a response, commonly in JSON format.

In simple terms:

1. Write your logic using Python.
2. Use Flask to expose that logic through API endpoints.
3. Accept inputs through HTTP requests.
4. Process those inputs and return the results, typically in JSON format.

## What did I build?

For this project, I used an **IPL dataset** containing 20 columns and information about matches played across multiple years.

Using Flask, I implemented two APIs:

### 1. `/api/teams`

- Returns the list of teams that have participated in the IPL, based on the dataset.

### 2. `/api/teamvsteam`

- Accepts two team names as inputs (`team1` and `team2`).
- Calculates the total number of matches played between them.
- Returns the number of matches won by each team.
- Also provides the number of drawn/tied matches.

## What's next?

The interesting part about APIs is that we can expose as many functionalities as we need through different endpoints.

We can build our logic, expose it through URLs, and make it accessible to other applications or users.

Once deployed on a server, anyone with access to the API endpoint can send a request and receive an instant response without needing to run our Python code locally.

**That's it! This is my first step towards understanding API development and its practical applications.**