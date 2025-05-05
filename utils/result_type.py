from enum import Enum


class SubScriptResult(Enum):
    SUCCESS = "success"
    ABORT_SOFT = "abort_soft"
    ABORT_HARD = "abort_hard"
    ABORT_EXCEPTION = "abort_exception"
