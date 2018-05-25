from django import forms


class UserList(forms.Form):
    user_list = forms.FileField(
        label='Upload user list csv file'
    )
