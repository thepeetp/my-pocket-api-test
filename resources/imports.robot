*** Settings ***
Variables   ${env}.yaml
Library    ../libs/RequestLibrary.py     ${account_url}     ${user_url}     ${expense_url}
Library     ../libs/common.py