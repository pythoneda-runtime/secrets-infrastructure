# vim: set fileencoding=utf-8
"""
pythoneda/runtime/secrets/infrastructure/dbus/secrets_dbus_signal_emitter.py

This file defines the SecretsDbusSignalEmitter class.

Copyright (C) 2024-today rydnr's pythoneda-runtime/secrets-infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.shared.infrastructure.dbus import DbusSignalEmitter
from typing import List


class SecretsDbusSignalEmitter(DbusSignalEmitter):
    """
    A Port that emits Secrets events as d-bus signals.

    Class name: SecretsDbusSignalEmitter

    Responsibilities:
        - Connect to d-bus.
        - Emit Secrets events as d-bus signals.

    Collaborators:
        - pythoneda.shared.application.PythonEDA: Requests emitting events.
        - pythoneda.shared.runtime.secrets.events.*
        - pythoneda.shared.runtime.secrets.events.infrastructure.dbus.*
    """

    def __init__(self):
        """
        Creates a new SecretsDbusSignalEmitter instance.
        """
        super().__init__()

    @classmethod
    def event_packages(cls) -> List[str]:
        """
        Retrieves the packages of the supported events.
        :return: The packages.
        :rtype: List[str]
        """
        return ["pythoneda.runtime.secrets.events.infrastructure.dbus"]


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
