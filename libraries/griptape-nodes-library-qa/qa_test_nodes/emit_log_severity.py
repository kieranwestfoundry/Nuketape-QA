import logging
from enum import StrEnum
from typing import Any

from griptape_nodes.exe_types.core_types import Parameter
from griptape_nodes.exe_types.node_types import ControlNode
from griptape_nodes.exe_types.param_types.parameter_string import ParameterString
from griptape_nodes.traits.options import Options

logger = logging.getLogger("griptape_nodes")


class Severity(StrEnum):
    WARNING = "WARNING"
    ERROR = "ERROR"


class EmitLogSeverity(ControlNode):
    """QA helper: emit a WARNING or ERROR into the engine log on demand."""

    def __init__(self, name: str, metadata: dict[Any, Any] | None = None) -> None:
        super().__init__(name, metadata)

        self.add_parameter(
            ParameterString(
                name="severity",
                default_value=Severity.WARNING.value,
                traits={Options(choices=[s.value for s in Severity])},
                tooltip="Which log level to emit",
            )
        )
        self.add_parameter(
            ParameterString(
                name="message",
                default_value="QA test message",
                tooltip="Message written to the log",
                multiline=True,
            )
        )
        self.add_parameter(
            Parameter(
                name="passthrough",
                type="any",
                default_value=None,
                tooltip="[Optional] Value passed straight through to the output",
            )
        )
        self.add_parameter(
            ParameterString(
                name="output",
                tooltip="What was emitted",
                allow_input=False,
                allow_property=False,
                allow_output=True,
            )
        )

    def process(self) -> None:
        severity = self.get_parameter_value("severity")
        message = self.get_parameter_value("message") or ""
        log_line = f"[{self.name}] {message}"

        self.parameter_output_values["passthrough"] = self.get_parameter_value("passthrough")
        self.parameter_output_values["output"] = f"{severity}: {log_line}"

        match severity:
            case Severity.WARNING:
                logger.warning(log_line)
            case Severity.ERROR:
                # Raising is what produces NodeErrorEvent, the only error path the Nuke bridge forwards.
                raise RuntimeError(log_line)
            case _:
                msg = f"Unknown severity: {severity!r}"
                raise ValueError(msg)
