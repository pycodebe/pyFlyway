class ReturnError(Exception):
    """
    Raised when pyFlyway returns an error, and there
    isn't a more specific subclass that represents the situation.
    """
    pass


class NoSchemaFoundError(Exception):
    """
    Raised when the configurqtion file does not not contain 
    any schema.
    """
    pass



class CleanForbiddenError(ReturnError):
    """
    Raised when pyFlyway tries of using clean command with 
    it has been disable in the configuration.
    """


class CleanError(ReturnError):
    """
    Raised when pyFlyway raise an exception with Clean command
    """
    pass


class VersionError(ReturnError):
    """
    Raised when pyFlyway raise an exception with Version command
    """
    pass


class MigrateError(ReturnError):
    """
    Raised when pyFlyway raise an exception with Migrate command
    """
    pass


class RepairError(ReturnError):
    """
    Raised when pyFlyway raise an exception with Repair command
    """
    pass


class BaselineError(ReturnError):
    """
    Raised when pyFlyway raise an exception with Baseline command
    """
    pass