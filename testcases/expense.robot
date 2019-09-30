*** Settings ***
Resource   ../keywords/create_user.robot
Resource    ../resources/imports.robot
Test Setup   Have a User

*** Variables ***
${date}      2019-09-29
${monthly}     201909

*** Test Cases ***
Create Expense
     When Add Expense    apple    50     ${date}
     Then Should Have a Expense    apple    50    ${date}


Delete Expense
    Given Have a Expense    apple    50     ${date}
    When Delete Expense
    Then Should Have no Expense


Get Suggestion
    When Add Expense    apple    50     ${date}
    And Add Expense    banana    50     ${date}
    Then Suggestion Should Contains     apple
    And Suggestion Should Contains     banana

Get Expense Daily
    When Add Expense    apple    50     ${date}
    And Add Expense    banana    90     ${date}
    Then Expense Dialy Should Be     140


Get Expense Monthly
    When Add Expense    apple    50     ${date}
    And Add Expense    banana    90     ${date}
    Then Expense Monthly Should Be     140

Get Expense Monthly Detail
    When Add Expense    banana    60     ${date}
    And Add Expense    apple    50     ${date}
    Then Expense Monthly Detail Should Contains    0    banana    60
    And Expense Monthly Detail Should Contains    1    apple     50



*** Keywords ***
Add Expense
    [Arguments]    ${description}      ${amount}      ${date}
    ${response}=     Request Create Expense      ${description}     ${amount}      ${date}     ${user_ref}
    Set Test Variable     ${response}

Have a Expense
    [Arguments]    ${description}      ${amount}      ${date}
    Add Expense     ${description}      ${amount}      ${date}
    Set Test Variable     ${expense_id}     ${response.json()['id']}

Delete Expense
    Request Delete Expense     ${expense_id}

Should Have a Expense
    [Arguments]    ${description}      ${amount}      ${date}
    ${response}=    Request Get Expenses     ${date}     ${user_ref}
    Should Be Equal As Strings     ${response.json()[0]['description']}     ${description}
    Should Be Equal As Numbers     ${response.json()[0]['amount']}     ${amount}

Should Have no Expense
    ${response}=    Request Get Expenses     ${date}     ${user_ref}
    Should Be Empty      ${response.json()}


Suggestion Should Contains
    [Arguments]    ${text}
    ${response}=     Request Get Suggestion     ${user_ref}
    Should Contain     ${response.json()}    ${text}

Expense Dialy Should Be
    [Arguments]    ${amount}
    ${response}=     Request Get Expense Daily     ${user_ref}
    Should Be Equal As Numbers      ${response.json()[0]['amount']}     ${amount}


Expense Monthly Should Be
    [Arguments]    ${amount}
    ${response}=     Request Get Expense Monthly     ${user_ref}
    Should Be Equal As Numbers      ${response.json()[0]['amount']}     ${amount}

Expense Monthly Detail Should Contains
    [Arguments]    ${index}    ${description}    ${amount}
    ${response}=     Request Get Expense Monthly Detail     ${user_ref}     ${monthly}
    Should Be Equal As Numbers     ${response.json()[${index}]['amount']}     ${amount}
    Should Be Equal As Strings     ${response.json()[${index}]['key']}     ${description}