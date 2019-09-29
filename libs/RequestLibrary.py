import requests


def request_create_account(name, balance, user_ref):
    response = requests.post('https://account-node.herokuapp.com/accounts', json={
                'name': name,
                'balance': balance,
                'userRef': user_ref
    }, headers={
        'Content-Type': 'application/json',
        'User-Ref': user_ref
    })

    print(response.text)
    return response


def request_get_accounts(user_ref):
    return requests.get('https://account-node.herokuapp.com/accounts', headers={
        'Content-Type': 'application/json',
        'User-Ref': user_ref
    })


def request_delete_account(account_id):
    return requests.delete('https://account-node.herokuapp.com/accounts/' + account_id)


def request_update_account(account_id, balance):
    print(account_id)
    return requests.put('https://account-node.herokuapp.com/accounts/' + account_id, json={
        'balance': balance
    })


def request_create_user(username, password):
    response = requests.post('https://user-node.herokuapp.com/users', json={
        'username': username,
        'password': password
    })
    print(response.text)
    return response


def request_login(username, password):
    return requests.post('https://user-node.herokuapp.com/users/login', json={
        'username': username,
        'password': password
    })

def request_create_expense(description, amount, date, user_ref):
    return requests.post('https://expense-node.herokuapp.com/expenses', json={
        'description': description,
        'amount': int(amount),
        'date': date
    }, headers={
        'Content-Type': 'application/json',
        'User-Ref': user_ref
    })


def request_get_expenses(date, user_ref):
    return requests.get('https://expense-node.herokuapp.com/expenses', params={
        'date': date
    }, headers={
        'Content-Type': 'application/json',
        'User-Ref': user_ref
    })


def request_delete_expense(id):
    return requests.delete('https://expense-node.herokuapp.com/expenses/' + id)


def request_get_suggestion(user_ref):
    return requests.get('https://expense-node.herokuapp.com/expenses/suggestion', headers={
        'Content-Type': 'application/json',
        'User-Ref': user_ref
    })


def request_get_expense_daily(user_ref):
    return requests.get('https://expense-node.herokuapp.com/expenses/dailyReport', headers={
        'Content-Type': 'application/json',
        'User-Ref': user_ref
    })


def request_get_expense_monthly(user_ref):
    return requests.get('https://expense-node.herokuapp.com/expenses/monthlyReport', headers={
        'Content-Type': 'application/json',
        'User-Ref': user_ref
    })
