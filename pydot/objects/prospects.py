class Prospects():
    """
    A class to query and use Pardot prospects.
    Prospect field reference: http://developer.pardot.com/kb/api-version-3/object-field-references#prospect
    """

    def __init__(self, client):
        self.client = client

    def query(self, **kwargs):
        """
        Returns the prospects matching the specified criteria parameters.
        Supported search parameters: http://developer.pardot.com/kb/api-version-3/querying-prospects#supported-search-criteria
        ex: client.Prospects.query(created_after='yesterday', assigned='false', limit=100)
        """
        result = self._get(path='/do/query', params=kwargs)
        return result

    def assign_by_email(self, email=None, **kwargs):
        """
        Assigns or reassigns the prospect specified by <email> to a specified Pardot user or
        group. One (and only one) of the following parameters must be provided to identify the target user or
        group: <user_email>, <user_id>, or <group_id>. Returns an updated version of the prospect.
        """
        kwargs['email'] = email
        result = self._post(path='/do/assign/email/{email}'.format(email=kwargs.get('email')), params=kwargs)
        return result

    def assign_by_id(self, id=None, **kwargs):
        """
        Assigns or reassigns the prospect specified by <id> to a specified Pardot user or
        group. One (and only one) of the following parameters must be provided to identify the target user or
        group: <user_email>, <user_id>, or <group_id>. Returns an updated version of the prospect.
        """
        kwargs['id'] = id
        result = self._post(path='/do/assign/id/{id}'.format(id=kwargs.get('id')), params=kwargs)
        return result

    def unassign_by_email(self, email=None, **kwargs):
        """Unassigns the prospect specified by <email>. Returns an updated version of the prospect."""
        result = self._post(path='/do/unassign/email/{email}'.format(email=kwargs.get('email')), params=kwargs)
        return result

    def unassign_by_id(self, id=None, **kwargs):
        """Unassigns the prospect specified by <id>. Returns an updated version of the prospect."""
        kwargs['id'] = id
        result = self._post(path='/do/unassign/id/{id}'.format(id=kwargs.get('id')), params=kwargs)
        return result

    def create(self, **kwargs):
        """
        Creates a new prospect using the specified data. <email> must be a unique email address. Returns the new prospect.
        """
        result = self._post(path='/do/create/email/{email}'.format(email=kwargs.get('email')), params=kwargs)
        return result

    def read_by_email(self, email=None, **kwargs):
        """
        Returns data for the prospect specified by <email>, including campaign assignment, profile criteria
        matching statuses, associated visitor activities, email list subscriptions, and custom field data.
        <email> is the email address of the target prospect.
        """
        kwargs['email'] = email
        result = self._post(path='/do/read/email/{email}'.format(email=kwargs.get('email')), params=kwargs)
        return result

    def read_by_id(self, id=None, **kwargs):
        """
        Returns data for the prospect specified by <id>, including campaign assignment, profile criteria
        matching statuses, associated visitor activities, email list subscriptions, and custom field data.
        <id> is the Pardot ID of the target prospect.
        """
        kwargs['id'] = id
        result = self._post(path='/do/read/id/{id}'.format(id=kwargs.get('id')), params=kwargs)
        return result

    def update_by_email(self, email=None, **kwargs):
        """
        Updates the provided data for a prospect specified by <email>. <email> is the email address of the
        prospect. Fields that are not updated by the request remain unchanged.nEmail list subscriptions and custom
        field data may also be updated with this request.
        """
        kwargs['email'] = email
        result = self._post(path='/do/update/email/{email}'.format(email=kwargs.get('email')), params=kwargs)
        return result

    def update_by_id(self, id=None, **kwargs):
        """
        Updates the provided data for a prospect specified by <id>. <id> is the Pardot ID of the prospect.
        Fields that are not updated by the request remain unchanged. Email list subscriptions and custom field data
        may also be updated with this request.
        """
        kwargs['id'] = id
        result = self._post(path='/do/update/id/{id}'.format(id=kwargs.get('id')), params=kwargs)
        return result

    def upsert_by_email(self, email=None, **kwargs):
        """
        Updates the provided data for the prospect specified by <email>. If a prospect with the provided email address
        does not yet exist, a new prospect is created using the <email> value. Fields that are not updated by the
        request remain unchanged. Email list subscriptions and custom field data may also be updated with this request.
        """
        kwargs['email'] = email
        result = self._post(path='/do/upsert/email/{email}'.format(email=kwargs.get('email')), params=kwargs)
        return result

    def upsert_by_id(self, id=None, email=None, **kwargs):
        """
        Updates the provided data for the prospect specified by <id>. If an <email> value is provided, it is used to
        update the prospect's email address. If a prospect with the provided ID is not found, Pardot searches for a
        prospect identified by <email>. If a prospect with the provided email address does not yet exist, a new
        prospect is created using <email> value. Fields that are not updated by the request remain unchanged.
        Email list subscriptions and custom field data may also be updated with this request.
        """
        kwargs['id'] = id
        kwargs['email'] = email
        result = self._post(path='/do/upsert/id/{id}'.format(id=kwargs.get('id')), params=kwargs)
        return result

    def delete_by_email(self, email=None, **kwargs):
        """Deletes the prospect specified by <email>. Returns True if operation was successful."""
        kwargs['email'] = email
        result = self._post(path='/do/delete/email/{email}'.format(email=kwargs.get('email')), params=kwargs)
        if result == 204:
            return True
        return False

    def delete_by_id(self, id=None, **kwargs):
        """Deletes the prospect specified by <id>. Returns True if operation was successful."""
        kwargs['id'] = id
        result = self._post(path='/do/delete/id/{id}'.format(id=kwargs.get('id')), params=kwargs)
        if result == 204:
            return True
        return False

    def _get(self, path=None, params={}):
        """GET requests for the Prospect object"""
        result = self.client._get(object='prospect', path=path, params=params)
        return result

    def _post(self, path=None, params={}):
        """POST requests for the Prospect object"""
        result = self.client._post(object='prospect', path=path, params=params)
        return result


