*** Variables ***

${SERVER}               http://localhost:55001/
${BROWSER}              firefox


*** Settings ***

Documentation   Django Robot Tests
Library         Selenium2Library  timeout=10  implicit_wait=0
Library         DjangoLibrary  127.0.0.1  55001  path=demo/myserver  manage=demo/manage.py  settings=myserver.settings  db=demo/db.sqlite3

Suite Setup     Start Django and open Browser
Suite Teardown  Stop Django and close Browser


*** Keywords ***

Start Django and open Browser
  Start Django
  Open Browser  ${SERVER}  ${BROWSER}

Stop Django and close browser
  Close Browser
  Stop Django

Open Browser To Login Page
  Open Browser  ${SERVER}  ${BROWSER}
  Maximize Browser Window


*** Test Cases ***

Scenario: As a visitor I can visit the django default page
  Go To  ${SERVER}
  Wait until page contains element  css=.jumbotron
  Page Should Contain  Schemaform Demo
