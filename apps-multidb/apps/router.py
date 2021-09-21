

class Router:
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'users':
            return app_label == 'accounts'
        else:
            return app_label != 'accounts'
