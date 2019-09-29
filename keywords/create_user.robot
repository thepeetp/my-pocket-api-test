*** Settings ***
Library     ../libs/RequestLibrary.py
Library     ../libs/common.py


*** Keywords ***
Have a User
    ${username}=     Generate Username
    Request Create User     ${username}     1234
    ${response}=    Request Login     ${username}     1234
    Set Suite Variable     ${user_ref}     ${response.text}