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
Disclaimer: this code has been validated with Gemini 1.0 Pro Vision.

You need to insert your project ID and selected region within `main.py`:

    project_id = 'your-project-id'
    region = 'your-region'

After editing the file, zip both the cloud function files (`main.py` and `requirements.txt`) as a ZIP file (more info on the archive structure [here](https://cloud.google.com/functions/docs/writing#directory-structure)). 

The settings for your cloud function should be:
* **Function Name**: driving-license-webhook
* **Environment**: 1st Gen
* **Region**: your desired region
* **Runtime**: Python 3.12
* **Timeout**: 60 seconds (this is very important, since Gemini takes some time to return)
* **Entry Point**: validate_driving_license
* Allow all traffic (being a demo, I've relaxed my security requirements)
* **Source**: the ZIP file you've just created

Feel free to deploy the cloud function using the Google Cloud Console or `gcloud` command. More info [here](https://cloud.google.com/functions/docs/deploy#basics).

#### Dialogflow Messenger (via Google App Engine)

#### Dialogflow CX Agent
