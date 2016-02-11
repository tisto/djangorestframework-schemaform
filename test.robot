*** Variables ***

${HOSTNAME}             127.0.0.1
${PORT}                 55001
${SERVER}               http://${HOSTNAME}:${PORT}/
${BROWSER}              firefox
${DJANGO_PATH}          demo/myserver
${DJANGO_MANAGE_PY}     demo/manage.py
${DJANGO_SETTINGS}      myserver.settings
${DJANGO_DB}            demo/db.sqlite3


*** Settings ***

Documentation   Django Robot Tests
Library         Selenium2Library  timeout=10  implicit_wait=3
Library         AngularJSLibrary
Library         DjangoLibrary  ${HOSTNAME}  ${PORT}  path=${DJANGO_PATH}  manage=${DJANGO_MANAGE_PY}  settings=${DJANGO_SETTINGS}  db=${DJANGO_DB}
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
  Wait for Angular
  Log Source
  Wait until page contains element  css=.jumbotron
  Page Should Contain  Schemaform Demo
  Click Link  Application
  Wait for Angular
  Page should contain element  xpath=//input[@ng-model="model['id']"]
  Click Link  User
  Wait for Angular
  Page should contain element  xpath=//input[@ng-model="model['id']"]

