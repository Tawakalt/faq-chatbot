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

## sales form
* contact_sales: Please connect me to someone from sales
  - sales_form

## greet + ask rasa x + ask channels + ask languages + sales form + thank + goodbye
* greet: Hello
    - utter_greet
* faq: I want information about rasa x
  - respond_faq
* faq: What channels of communication does rasa support?
  - respond_faq
* faq: what language does rasa support?
  - respond_faq
* contact_sales: I want to get in touch with your sales guys
  - sales_form
* thank: Thanks for that
    - utter_noworries
* bye: Goodbye
    - utter_bye

## sales form + explain job function
* contact_sales: I would like to talk to someone from your sales team
  - sales_form
  - slot{"requested_slot": "job_function"}
* explain: could you explain why you need it?
  - utter_explain_why_job_function
  - sales_form

## sales form + explain use case
* contact_sales: sales please
  - sales_form
  - slot{"requested_slot": "use_case"}
* explain: why do you need it?
  - utter_explain_why_use_case
  - sales_form

## sales form + explain budget
* contact_sales: I want to speak with sales
  - sales_form
  - slot{"requested_slot": "budget"}
* explain: why do you need to know that?
  - utter_explain_why_budget
  - sales_form

## sales form + explain name
* contact_sales: I wanna talk to your sales people.
  - sales_form
  - slot{"requested_slot": "person_name"}
* explain: why is that?
  - utter_explain_why_name
  - sales_form

## sales form + explain company
* contact_sales: Sales
  - sales_form
  - slot{"requested_slot": "company"}
* explain: why?
  - utter_explain_why_company
  - sales_form

## sales form + explain email
* contact_sales: I want to get in touch with your sales guys
  - sales_form
  - slot{"requested_slot": "business_email"}
* explain: what for?
  - utter_explain_why_email
  - sales_form