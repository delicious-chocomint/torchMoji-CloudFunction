# torchMoji-CloudFunction

Forked from [😇 torchMoji](https://github.com/huggingface/torchMoji).
Updated dependencies, and made minor edits to enable the code to run on python 3.7.
Modified for deployment to Google Cloud Functions, for a RESTful API.

```
// sample request
https://xxxxx.cloudfunctions.net/textToEmoji?text=I%20know%20good%20movies,%20this%20ain%27t%20one
// data response
{
  "emoji0": "🙅",
  "emoji0_emotion": "Disapproval",
  "emoji1": "💯",
  "emoji1_emotion": "Amazement",
  "emoji2": "✋",
  "emoji2_emotion": "Dismay",
  "emoji3": "😌",
  "emoji3_emotion": "Optimism",
  "emoji4": "😏",
  "emoji4_emotion": "Amusement"
}
```

Note that a response may take 10~20 seconds, due to the nature of cloud functions.

# Setup

1. Download the pretrained torchMoji weights from [here](https://www.dropbox.com/s/q8lax9ary32c7t9/pytorch_model.bin?dl=0) and put them in the `torchMojiAPI/model` directory
1. Set up a Google cloud project and install the Cloud SDK with instructions from [link](https://cloud.google.com/functions/docs/first-python#creating_a_gcp_project_using_cloud_sdk)
1. In [torchMojiAPI](torchMojiAPI) run `gcloud functions deploy textToEmoji --runtime python37 --memory 512MB --trigger-http --allow-unauthenticated`
1. Keep note of the `httpsTrigger` URL returned by the output, or run `gcloud functions describe textToEmoji` for the API URL.
