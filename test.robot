*** Variables ***

${HOSTNAME}             127.0.0.1
${PORT}                 55001
${SERVER}               http://${HOSTNAME}:${PORT}/
${BROWSER}              firefox


*** Settings ***

Documentation   Django Robot Tests
Library         Selenium2Library  timeout=10  implicit_wait=0
Library         DjangoLibrary  ${HOSTNAME}  ${PORT}  path=demo/myserver  manage=demo/manage.py  settings=myserver.settings  db=demo/db.sqlite3
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
  Click Link  Application
  Wait until page contains   Model
  Page should contain element  xpath=//input[@ng-model="model['id']"]
  Click Link  User
  Wait until page contains   Model
  Page should contain element  xpath=//input[@ng-model="model['id']"]

