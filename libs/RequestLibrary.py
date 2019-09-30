import requests


class RequestLibrary:

    def __init__(self, account_url, user_url, expense_url):
        self.account_url = account_url
        self.user_url = user_url
        self.expense_url = expense_url

    def request_create_account(self, name, balance, user_ref):
        response = requests.post(self.account_url, json={
                    'name': name,
                    'balance': balance,
                    'userRef': user_ref
        }, headers={
            'Content-Type': 'application/json',
            'User-Ref': user_ref
        })

        print(response.text)
        return response

    def request_get_accounts(self, user_ref):
        return requests.get(self.account_url, headers={
            'Content-Type': 'application/json',
            'User-Ref': user_ref
        })

    def request_delete_account(self, account_id, user_ref):
        return requests.delete(self.account_url + '/' + account_id, headers={
            'Content-Type': 'application/json',
            'User-Ref': user_ref
        })

    def request_update_account(self, account_id, balance, user_ref):
        print(account_id)
        return requests.put(self.account_url + '/' + account_id, json={
            'balance': balance
        }, headers={
            'Content-Type': 'application/json',
            'User-Ref': user_ref
        })


    def request_create_user(self, username, password):
        response = requests.post(self.user_url, json={
            'username': username,
            'password': password
        })
        print(response.text)
        return response

    def request_login(self, username, password):
        return requests.post(self.user_url + '/login', json={
            'username': username,
            'password': password
        })

    def request_create_expense(self, description, amount, date, user_ref):
        return requests.post(self.expense_url, json={
            'description': description,
            'amount': int(amount),
            'date': date
        }, headers={
            'Content-Type': 'application/json',
            'User-Ref': user_ref
        })

    def request_get_expenses(self, date, user_ref):
        return requests.get(self.expense_url, params={
            'date': date
        }, headers={
            'Content-Type': 'application/json',
            'User-Ref': user_ref
        })

    def request_delete_expense(self, id, user_ref):
        return requests.delete(self.expense_url + '/' + id, headers={
            'Content-Type': 'application/json',
            'User-Ref': user_ref
        })

    def request_get_suggestion(self, user_ref):
        return requests.get(self.expense_url + '/suggestion', headers={
            'Content-Type': 'application/json',
            'User-Ref': user_ref
        })

    def request_get_expense_daily(self, user_ref):
        return requests.get(self.expense_url + '/dailyReport', headers={
            'Content-Type': 'application/json',
            'User-Ref': user_ref
        })

    def request_get_expense_monthly(self, user_ref):
        return requests.get(self.expense_url + '/monthlyReport', headers={
            'Content-Type': 'application/json',
            'User-Ref': user_ref
        })

    def request_get_expense_monthly_detail(self, user_ref, monthly_keyword):
        return requests.get(self.expense_url + '/monthlyReport/' + monthly_keyword, headers={
            'Content-Type': 'application/json',
            'User-Ref': user_ref
        })
