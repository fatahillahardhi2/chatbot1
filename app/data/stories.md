<!-- ## daftar
* greet
  - utter_greet
* nama{"tellName": "ardhi"}
  - slot {"tellName": "ardhi"}
  - action_name
  - utter_nama
* daftarAsk
  - utter_daftarAsk
* daftarDone
  - utter_daftarDone -->
## daftarPMDK happy path
* daftarAsk
  - utter_daftarAsk
* daftarPMDK
  - utter_daftarPMDK
  - utter_daftarAfterResponse
* daftarDone
  - utter_daftarDone

## daftarPMDK langsung
* daftarPMDK
  - utter_daftarPMDK
  - utter_daftarAfterResponse
* daftarDone
  - utter_daftarDone

## daftarUSM happy path
* daftarAsk
  - utter_daftarAsk
* daftarUSM
  - utter_daftarUSM
  - utter_daftarAfterResponse
* daftarDone
  - utter_daftarDone

## daftarUSM langsung
* daftarUSM
  - utter_daftarUSM
  - utter_daftarAfterResponse
* daftarDone
  - utter_daftarDone

## daftarPMDK greet
* greet
  - utter_greet
* daftarAsk
  - utter_daftarAsk
* daftarPMDK
  - utter_daftarPMDK
  - utter_daftarAfterResponse

## daftarUSM greet
* greet
  - utter_greet
* daftarAsk
  - utter_daftarAsk
* daftarUSM
  - utter_daftarUSM
  - utter_daftarAfterResponse

## daftarDone
* daftarDone
  - utter_daftarDone

## daftarAskAgain
* again
  - utter_again





<!-- ## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot -->
