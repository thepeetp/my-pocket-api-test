*** Settings ***
Resource   ../keywords/create_user.robot
Resource    ../resources/imports.robot
Test Setup   Have a User


*** Test Cases ***
Create Account
     When Create Account    Account A      100
     Then Should Have a Account     Account A      100


Update Account
    Given Have a Account    Account A      100
    When Update Balance     500
    Then Should Have a Account     Account A      500


Delete Account
    Given Have a Account
    When Delete Account
    Then Should Have No Account



*** Keywords ***
Have a Account
    [Arguments]      ${name}=Account A      ${balance}=100
    Create Account     ${name}     ${balance}
    Set Test Variable     ${account_id}     ${response.text}

Delete Account
    Request Delete Account     ${account_id}


Update Balance
    [Arguments]     ${balance}
    Request Update Account     ${account_id}     ${balance}


Create Account
    [Arguments]      ${name}      ${balance}
    ${response}=     Request Create Account     ${name}    ${balance}    ${user_ref}
    Set Test Variable     ${response}

Should Have a Account
    [Arguments]     ${name}      ${balance}
    Should Not Be Empty     ${response.text}
    Should Be Equal as numbers     ${response.status_code}     200
    ${response}=     Request Get Accounts     ${user_ref}
    Should Be Equal as Numbers    ${response.json()[0]['balance']}    ${balance}
    Should Be Equal as Strings    ${response.json()[0]['name']}      ${name}


Should Have No Account
    ${response}=     Request Get Accounts     ${user_ref}
    Should Be Empty     ${response.json()}