# Create multimodal conversational experiences with Google Cloud Dialogflow CX and Gemini Vision
**Latest Update: 19/04/2024**

### Intro
This is the companion repo of the Medium blog [Create multimodal conversational experiences with Google Cloud Dialogflow CX and Gemini Vision](https://medium.com/p/8d39035b985d). If you haven't read the article, my first advise is to start from there.

This repo contains a working prototype of the agent described in the article, mainly for learning purposes. Feel free to check-out the repo and re-use according to the licensing terms.

### Repo Structure
This repo contains three main artifacts:
* An intent-based [Dialogflow CX](https://cloud.google.com/dialogflow/cx/docs/basics) agent;
* A [Google Cloud Function](https://cloud.google.com/functions/), invoked by the agent via a [webhook](https://cloud.google.com/dialogflow/cx/docs/concept/webhook);
* A webapp (in my case I've deployed it on [Google App Engine](https://cloud.google.com/appengine/)), embedding a [Dialogflow Messenger](https://cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger) widget, to interact with the agent deployed on the back-end.

### Architecture
The aforementioned artifacts implement the following architecture.
![dfcx + gemini vision architecture](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*cDhKstGBgzgTughh)

### Setup
This is the procedure to setup the whole prototype. Feel free to change some of the configurations according to your needs.

#### Google Cloud Functions

#### Dialogflow Messenger (via Google App Engine)

#### Dialogflow CX Agent
