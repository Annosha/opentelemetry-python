"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2020, OpenTelemetry Authors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import opentelemetry.proto.common.v1.common_pb2
import opentelemetry.proto.resource.v1.resource_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _SeverityNumber:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SeverityNumberEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _SeverityNumber.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SEVERITY_NUMBER_UNSPECIFIED: _SeverityNumber.ValueType  # 0
    """UNSPECIFIED is the default SeverityNumber, it MUST NOT be used."""
    SEVERITY_NUMBER_TRACE: _SeverityNumber.ValueType  # 1
    SEVERITY_NUMBER_TRACE2: _SeverityNumber.ValueType  # 2
    SEVERITY_NUMBER_TRACE3: _SeverityNumber.ValueType  # 3
    SEVERITY_NUMBER_TRACE4: _SeverityNumber.ValueType  # 4
    SEVERITY_NUMBER_DEBUG: _SeverityNumber.ValueType  # 5
    SEVERITY_NUMBER_DEBUG2: _SeverityNumber.ValueType  # 6
    SEVERITY_NUMBER_DEBUG3: _SeverityNumber.ValueType  # 7
    SEVERITY_NUMBER_DEBUG4: _SeverityNumber.ValueType  # 8
    SEVERITY_NUMBER_INFO: _SeverityNumber.ValueType  # 9
    SEVERITY_NUMBER_INFO2: _SeverityNumber.ValueType  # 10
    SEVERITY_NUMBER_INFO3: _SeverityNumber.ValueType  # 11
    SEVERITY_NUMBER_INFO4: _SeverityNumber.ValueType  # 12
    SEVERITY_NUMBER_WARN: _SeverityNumber.ValueType  # 13
    SEVERITY_NUMBER_WARN2: _SeverityNumber.ValueType  # 14
    SEVERITY_NUMBER_WARN3: _SeverityNumber.ValueType  # 15
    SEVERITY_NUMBER_WARN4: _SeverityNumber.ValueType  # 16
    SEVERITY_NUMBER_ERROR: _SeverityNumber.ValueType  # 17
    SEVERITY_NUMBER_ERROR2: _SeverityNumber.ValueType  # 18
    SEVERITY_NUMBER_ERROR3: _SeverityNumber.ValueType  # 19
    SEVERITY_NUMBER_ERROR4: _SeverityNumber.ValueType  # 20
    SEVERITY_NUMBER_FATAL: _SeverityNumber.ValueType  # 21
    SEVERITY_NUMBER_FATAL2: _SeverityNumber.ValueType  # 22
    SEVERITY_NUMBER_FATAL3: _SeverityNumber.ValueType  # 23
    SEVERITY_NUMBER_FATAL4: _SeverityNumber.ValueType  # 24

class SeverityNumber(
    _SeverityNumber, metaclass=_SeverityNumberEnumTypeWrapper
):
    """Possible values for LogRecord.SeverityNumber."""

SEVERITY_NUMBER_UNSPECIFIED: SeverityNumber.ValueType  # 0
"""UNSPECIFIED is the default SeverityNumber, it MUST NOT be used."""
SEVERITY_NUMBER_TRACE: SeverityNumber.ValueType  # 1
SEVERITY_NUMBER_TRACE2: SeverityNumber.ValueType  # 2
SEVERITY_NUMBER_TRACE3: SeverityNumber.ValueType  # 3
SEVERITY_NUMBER_TRACE4: SeverityNumber.ValueType  # 4
SEVERITY_NUMBER_DEBUG: SeverityNumber.ValueType  # 5
SEVERITY_NUMBER_DEBUG2: SeverityNumber.ValueType  # 6
SEVERITY_NUMBER_DEBUG3: SeverityNumber.ValueType  # 7
SEVERITY_NUMBER_DEBUG4: SeverityNumber.ValueType  # 8
SEVERITY_NUMBER_INFO: SeverityNumber.ValueType  # 9
SEVERITY_NUMBER_INFO2: SeverityNumber.ValueType  # 10
SEVERITY_NUMBER_INFO3: SeverityNumber.ValueType  # 11
SEVERITY_NUMBER_INFO4: SeverityNumber.ValueType  # 12
SEVERITY_NUMBER_WARN: SeverityNumber.ValueType  # 13
SEVERITY_NUMBER_WARN2: SeverityNumber.ValueType  # 14
SEVERITY_NUMBER_WARN3: SeverityNumber.ValueType  # 15
SEVERITY_NUMBER_WARN4: SeverityNumber.ValueType  # 16
SEVERITY_NUMBER_ERROR: SeverityNumber.ValueType  # 17
SEVERITY_NUMBER_ERROR2: SeverityNumber.ValueType  # 18
SEVERITY_NUMBER_ERROR3: SeverityNumber.ValueType  # 19
SEVERITY_NUMBER_ERROR4: SeverityNumber.ValueType  # 20
SEVERITY_NUMBER_FATAL: SeverityNumber.ValueType  # 21
SEVERITY_NUMBER_FATAL2: SeverityNumber.ValueType  # 22
SEVERITY_NUMBER_FATAL3: SeverityNumber.ValueType  # 23
SEVERITY_NUMBER_FATAL4: SeverityNumber.ValueType  # 24
global___SeverityNumber = SeverityNumber

class _LogRecordFlags:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _LogRecordFlagsEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _LogRecordFlags.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    LOG_RECORD_FLAGS_DO_NOT_USE: _LogRecordFlags.ValueType  # 0
    """The zero value for the enum. Should not be used for comparisons.
    Instead use bitwise "and" with the appropriate mask as shown above.
    """
    LOG_RECORD_FLAGS_TRACE_FLAGS_MASK: _LogRecordFlags.ValueType  # 255
    """Bits 0-7 are used for trace flags."""

class LogRecordFlags(
    _LogRecordFlags, metaclass=_LogRecordFlagsEnumTypeWrapper
):
    """LogRecordFlags represents constants used to interpret the
    LogRecord.flags field, which is protobuf 'fixed32' type and is to
    be used as bit-fields. Each non-zero value defined in this enum is
    a bit-mask.  To extract the bit-field, for example, use an
    expression like:

      (logRecord.flags & LOG_RECORD_FLAGS_TRACE_FLAGS_MASK)
    """

LOG_RECORD_FLAGS_DO_NOT_USE: LogRecordFlags.ValueType  # 0
"""The zero value for the enum. Should not be used for comparisons.
Instead use bitwise "and" with the appropriate mask as shown above.
"""
LOG_RECORD_FLAGS_TRACE_FLAGS_MASK: LogRecordFlags.ValueType  # 255
"""Bits 0-7 are used for trace flags."""
global___LogRecordFlags = LogRecordFlags

@typing_extensions.final
class LogsData(google.protobuf.message.Message):
    """LogsData represents the logs data that can be stored in a persistent storage,
    OR can be embedded by other protocols that transfer OTLP logs data but do not
    implement the OTLP protocol.

    The main difference between this message and collector protocol is that
    in this message there will not be any "control" or "metadata" specific to
    OTLP protocol.

    When new fields are added into this message, the OTLP request MUST be updated
    as well.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_LOGS_FIELD_NUMBER: builtins.int
    @property
    def resource_logs(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___ResourceLogs
    ]:
        """An array of ResourceLogs.
        For data coming from a single resource this array will typically contain
        one element. Intermediary nodes that receive data from multiple origins
        typically batch the data before forwarding further and in that case this
        array will contain multiple elements.
        """

    def __init__(
        self,
        *,
        resource_logs: (
            collections.abc.Iterable[global___ResourceLogs] | None
        ) = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "resource_logs", b"resource_logs"
        ],
    ) -> None: ...

global___LogsData = LogsData

@typing_extensions.final
class ResourceLogs(google.protobuf.message.Message):
    """A collection of ScopeLogs from a Resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_FIELD_NUMBER: builtins.int
    SCOPE_LOGS_FIELD_NUMBER: builtins.int
    SCHEMA_URL_FIELD_NUMBER: builtins.int
    @property
    def resource(
        self,
    ) -> opentelemetry.proto.resource.v1.resource_pb2.Resource:
        """The resource for the logs in this message.
        If this field is not set then resource info is unknown.
        """

    @property
    def scope_logs(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___ScopeLogs
    ]:
        """A list of ScopeLogs that originate from a resource."""
    schema_url: builtins.str
    """The Schema URL, if known. This is the identifier of the Schema that the resource data
    is recorded in. To learn more about Schema URL see
    https://opentelemetry.io/docs/specs/otel/schemas/#schema-url
    This schema_url applies to the data in the "resource" field. It does not apply
    to the data in the "scope_logs" field which have their own schema_url field.
    """
    def __init__(
        self,
        *,
        resource: (
            opentelemetry.proto.resource.v1.resource_pb2.Resource | None
        ) = ...,
        scope_logs: collections.abc.Iterable[global___ScopeLogs] | None = ...,
        schema_url: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["resource", b"resource"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "resource",
            b"resource",
            "schema_url",
            b"schema_url",
            "scope_logs",
            b"scope_logs",
        ],
    ) -> None: ...

global___ResourceLogs = ResourceLogs

@typing_extensions.final
class ScopeLogs(google.protobuf.message.Message):
    """A collection of Logs produced by a Scope."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCOPE_FIELD_NUMBER: builtins.int
    LOG_RECORDS_FIELD_NUMBER: builtins.int
    SCHEMA_URL_FIELD_NUMBER: builtins.int
    @property
    def scope(
        self,
    ) -> opentelemetry.proto.common.v1.common_pb2.InstrumentationScope:
        """The instrumentation scope information for the logs in this message.
        Semantically when InstrumentationScope isn't set, it is equivalent with
        an empty instrumentation scope name (unknown).
        """

    @property
    def log_records(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___LogRecord
    ]:
        """A list of log records."""
    schema_url: builtins.str
    """The Schema URL, if known. This is the identifier of the Schema that the log data
    is recorded in. To learn more about Schema URL see
    https://opentelemetry.io/docs/specs/otel/schemas/#schema-url
    This schema_url applies to all logs in the "logs" field.
    """
    def __init__(
        self,
        *,
        scope: (
            opentelemetry.proto.common.v1.common_pb2.InstrumentationScope
            | None
        ) = ...,
        log_records: collections.abc.Iterable[global___LogRecord] | None = ...,
        schema_url: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["scope", b"scope"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "log_records",
            b"log_records",
            "schema_url",
            b"schema_url",
            "scope",
            b"scope",
        ],
    ) -> None: ...

global___ScopeLogs = ScopeLogs

@typing_extensions.final
class LogRecord(google.protobuf.message.Message):
    """A log record according to OpenTelemetry Log Data Model:
    https://github.com/open-telemetry/oteps/blob/main/text/logs/0097-log-data-model.md
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIME_UNIX_NANO_FIELD_NUMBER: builtins.int
    OBSERVED_TIME_UNIX_NANO_FIELD_NUMBER: builtins.int
    SEVERITY_NUMBER_FIELD_NUMBER: builtins.int
    SEVERITY_TEXT_FIELD_NUMBER: builtins.int
    BODY_FIELD_NUMBER: builtins.int
    ATTRIBUTES_FIELD_NUMBER: builtins.int
    DROPPED_ATTRIBUTES_COUNT_FIELD_NUMBER: builtins.int
    FLAGS_FIELD_NUMBER: builtins.int
    TRACE_ID_FIELD_NUMBER: builtins.int
    SPAN_ID_FIELD_NUMBER: builtins.int
    time_unix_nano: builtins.int
    """time_unix_nano is the time when the event occurred.
    Value is UNIX Epoch time in nanoseconds since 00:00:00 UTC on 1 January 1970.
    Value of 0 indicates unknown or missing timestamp.
    """
    observed_time_unix_nano: builtins.int
    """Time when the event was observed by the collection system.
    For events that originate in OpenTelemetry (e.g. using OpenTelemetry Logging SDK)
    this timestamp is typically set at the generation time and is equal to Timestamp.
    For events originating externally and collected by OpenTelemetry (e.g. using
    Collector) this is the time when OpenTelemetry's code observed the event measured
    by the clock of the OpenTelemetry code. This field MUST be set once the event is
    observed by OpenTelemetry.

    For converting OpenTelemetry log data to formats that support only one timestamp or
    when receiving OpenTelemetry log data by recipients that support only one timestamp
    internally the following logic is recommended:
      - Use time_unix_nano if it is present, otherwise use observed_time_unix_nano.

    Value is UNIX Epoch time in nanoseconds since 00:00:00 UTC on 1 January 1970.
    Value of 0 indicates unknown or missing timestamp.
    """
    severity_number: global___SeverityNumber.ValueType
    """Numerical value of the severity, normalized to values described in Log Data Model.
    [Optional].
    """
    severity_text: builtins.str
    """The severity text (also known as log level). The original string representation as
    it is known at the source. [Optional].
    """
    @property
    def body(self) -> opentelemetry.proto.common.v1.common_pb2.AnyValue:
        """A value containing the body of the log record. Can be for example a human-readable
        string message (including multi-line) describing the event in a free form or it can
        be a structured data composed of arrays and maps of other values. [Optional].
        """

    @property
    def attributes(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        opentelemetry.proto.common.v1.common_pb2.KeyValue
    ]:
        """Additional attributes that describe the specific event occurrence. [Optional].
        Attribute keys MUST be unique (it is not allowed to have more than one
        attribute with the same key).
        """
    dropped_attributes_count: builtins.int
    flags: builtins.int
    """Flags, a bit field. 8 least significant bits are the trace flags as
    defined in W3C Trace Context specification. 24 most significant bits are reserved
    and must be set to 0. Readers must not assume that 24 most significant bits
    will be zero and must correctly mask the bits when reading 8-bit trace flag (use
    flags & LOG_RECORD_FLAGS_TRACE_FLAGS_MASK). [Optional].
    """
    trace_id: builtins.bytes
    """A unique identifier for a trace. All logs from the same trace share
    the same `trace_id`. The ID is a 16-byte array. An ID with all zeroes OR
    of length other than 16 bytes is considered invalid (empty string in OTLP/JSON
    is zero-length and thus is also invalid).

    This field is optional.

    The receivers SHOULD assume that the log record is not associated with a
    trace if any of the following is true:
      - the field is not present,
      - the field contains an invalid value.
    """
    span_id: builtins.bytes
    """A unique identifier for a span within a trace, assigned when the span
    is created. The ID is an 8-byte array. An ID with all zeroes OR of length
    other than 8 bytes is considered invalid (empty string in OTLP/JSON
    is zero-length and thus is also invalid).

    This field is optional. If the sender specifies a valid span_id then it SHOULD also
    specify a valid trace_id.

    The receivers SHOULD assume that the log record is not associated with a
    span if any of the following is true:
      - the field is not present,
      - the field contains an invalid value.
    """
    def __init__(
        self,
        *,
        time_unix_nano: builtins.int = ...,
        observed_time_unix_nano: builtins.int = ...,
        severity_number: global___SeverityNumber.ValueType = ...,
        severity_text: builtins.str = ...,
        body: opentelemetry.proto.common.v1.common_pb2.AnyValue | None = ...,
        attributes: (
            collections.abc.Iterable[
                opentelemetry.proto.common.v1.common_pb2.KeyValue
            ]
            | None
        ) = ...,
        dropped_attributes_count: builtins.int = ...,
        flags: builtins.int = ...,
        trace_id: builtins.bytes = ...,
        span_id: builtins.bytes = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["body", b"body"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "attributes",
            b"attributes",
            "body",
            b"body",
            "dropped_attributes_count",
            b"dropped_attributes_count",
            "flags",
            b"flags",
            "observed_time_unix_nano",
            b"observed_time_unix_nano",
            "severity_number",
            b"severity_number",
            "severity_text",
            b"severity_text",
            "span_id",
            b"span_id",
            "time_unix_nano",
            b"time_unix_nano",
            "trace_id",
            b"trace_id",
        ],
    ) -> None: ...

global___LogRecord = LogRecord
