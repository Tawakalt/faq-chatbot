## greet
* greet
  - utter_greet

## thank
* thank
  - utter_noworries

## goodbye
* bye
  - utter_bye

## Some question from FAQ
* faq
    - respond_faq

## sales form
* contact_sales
    - sales_form                   <!--Run the sales_form action-->
    - form{"name": "sales_form"}   <!--Activate the form-->
    - form{"name": null}           <!--Deactivate the form-->

## Sales and faq
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
* faq
    - respond_faq
    - sales_form
    - form{"name": null}

## explain job function
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "job_function"}
* explain
    - utter_explain_why_job_function
    - sales_form
    - form{"name": null}

## explain use case
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "use_case"}
* explain
    - utter_explain_why_use_case
    - sales_form
    - form{"name": null}

## explain budget
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "budget"}
* explain
    - utter_explain_why_budget
    - sales_form
    - form{"name": null}

## explain name
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "person_name"}
* explain
    - utter_explain_why_name
    - sales_form
    - form{"name": null}

## explain company
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "company"}
* explain
    - utter_explain_why_company
    - sales_form
    - form{"name": null}

## explain email
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "business_email"}
* explain
    - utter_explain_why_email
    - sales_form
    - form{"name": null}

## out of scope
* out_of_scope
  - utter_out_of_scope