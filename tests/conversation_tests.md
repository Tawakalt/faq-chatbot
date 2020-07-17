## greet + goodbye
* greet: Hi
    - utter_greet
* bye: Bye
    - utter_bye

## greet + thank
* greet: Hello
    - utter_greet
* thank: Thanks a lot
    - utter_noworries

## thank + goodbye
* thank: Thank you very much
    - utter_noworries
* bye: See ya
    - utter_bye

## greet + thank + goodbye
* greet: Good Day
    - utter_greet
* thank: Thanks a lot
    - utter_noworries
* bye: Farewell
    - utter_bye

## ask channels
* faq: What messaging channels does Rasa support?
  - respond_faq

## ask languages
* faq: Which languages can I build assistants in?
  - respond_faq

## ask rasa x
* faq: What’s Rasa X?
  - respond_faq