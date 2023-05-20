

def detectUser(user):
    if user.role == 1:
        redirectUril = 'vendorDashboard'
        return redirectUril
    elif user.role == 2:
        redirectUril = 'custDashboard'
        return redirectUril
    elif user.role == None and user.is_superadmin:
        redirectUril = '/admin'
        return redirectUril