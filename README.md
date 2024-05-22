# Project Title [Ministry of Interior Hacakathon] [InnovateX]
Enhancing Accessibility and Engagement for All

## Description
### Problems
- Navigation challenges
- Accessibility issues for senior citizens and people with disabilities due to cumbersome website design
- Unresponsiveness

### Solutions
- Introducing an innovative MOI Assistant equipped with voice-to-text and sign language translation functionalities, aimed at simplifying service requests. Just express your needs verbally, and the assistant will handle the rest, enhancing consumer satisfaction and engagement, especially for people with disabilities, senior citizens, and the general public. This assistant utilizes machine learning and natural language understanding (NLU) conversational AI.
- Developing gamified software to make websites more engaging and accessible to everyone.
- Implementing advanced statistics for web data analytics.

## Features
1. **MOI Assistant**
2. **Gamification Features**
3. **Statistics Dashboard**

## Details

### MOI Assistant
- An integrated AI utilizing machine learning technology, natural language processing (NLP), and NLU software to perform various operations:
    1. Processing text inputs and providing responses based on trained data for MOI services.
    2. Converting audio input to text messages for processing and responding accordingly.
    3. Processing sign language input and delivering desired outputs based on pre-trained datasets.
- Simplified web app navigation tools, such as arrows for page navigation, improving the user interface for people with special needs.
- Accessibility tools for customizing the web app interface to cater to people with special needs and senior citizens.

### Gamification Features
- Incorporating powerful features to gamify numerous services on the MOI website, saving time, space, and memory.
- Enhancing user engagement, retention, and ease of finding required services.

### Statistics Dashboard
- Providing a dashboard for monitoring web activities and determining user categories.

## Getting Started
1. Navigate to the MOI directory.
2. If Python is installed, execute `pip install -r requirements.txt` in the MOI directory to install all requirements.
3. Ensure all requirements are installed.
4. Run the Django server from the MOI directory using `make start` or `python manage.py runserver`. Keep the server running.
5. In another terminal, navigate to AI_MOI and run `make run` or `rasa run --enable-api -p 50055` to start the Rasa API. Wait for about 20 seconds for the API server to start.
6. Open another terminal, navigate to AI_MOI directory, and run `rasa run actions` to execute custom actions performed by Rasa during the training process.
7. If all servers (Django, Rasa API, Rasa actions) are running successfully, access the web app at http://127.0.0.1:8000.
8. Explore the functionalities including MOI Assistant, gamification features, and statistics dashboard.

## Dependencies
- Django
- Transformers
- Torch
- Pipenv
- Rasa
- OpenCV-Python (version 4.7.0.68)
- Mediapipe
- Scikit-learn (version 1.2.0)

## Installing
1. Start by installing dependencies with `pip install -r requirements.txt`.
2. Navigate to AI_MOI and run `make run` or ` rasa run --enable-api -p 50055`.
3. To run the Django server at port 8000, exit AI_MOI and navigate to MOI_Assistant, then run `make start` or ` python manage.py runserver`.

## Executing Program
- Run `rasa run actions`.
- Follow step-by-step instructions provided.

## Help
For common problems or issues, refer to the command to run if the program contains helper info.

## Authors
- [@AllanRye9](https://github.com/AllanRye9)
- [@pamone74](https://github.com/pamone74)

## Version History
- 0.1: MVP prototype
