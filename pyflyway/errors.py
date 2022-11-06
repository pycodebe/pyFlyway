# pylint: disable=missing-docstring


class ReturnError(Exception):
    """
    Raised when pyFlyway returns an error, and there
    isn't a more specific subclass that represents the situation.
    """


class NoSchemaFoundError(Exception):
    """
    Raised when the configurqtion file does not not contain
    any schema.
    """


class CleanForbiddenError(ReturnError):
    """
    Raised when pyFlyway tries of using clean command with
    it has been disable in the configuration.
    """


class CleanError(ReturnError):
    """
    Raised when pyFlyway raise an exception with Clean command
    """


class VersionError(ReturnError):
    """
    Raised when pyFlyway raise an exception with Version command
    """


class MigrateError(ReturnError):
    """
    Raised when pyFlyway raise an exception with Migrate command
    """


class RepairError(ReturnError):
    """
    Raised when pyFlyway raise an exception with Repair command
    """


class BaselineError(ReturnError):
    """
    Raised when pyFlyway raise an exception with Baseline command
    """
