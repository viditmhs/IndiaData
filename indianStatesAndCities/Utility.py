'''
    Author: Vidit Maheshwrai
    Date: 20170602
    Copyright :

    Purpose: Utility function specific to app

    History:

'''

def authentication(request):
    try:
        user_name = request.META['HTTP_USER_NAME']
        user_pass = request.META['HTTP_USER_PASSWORD']
        if(user_name == "Vidit" and user_pass == "Maheshwari"):
            return True
        else:
            return False
    except Exception as e:
        return False