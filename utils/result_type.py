from enum import Enum


class SubScriptResult(Enum):
    SUCCESS = "success"  # successful completion of a subscript
    ABORT_SOFT = (
        "abort_soft"  # soft abort from a subscript, rest of the program should continue
    )
    ABORT_HARD = "abort_hard"  # hard abort from a subscript, rest of the program should be aborted
    ABORT_EXCEPTION = "abort_exception"  # exception/error occurred
    ABORT_USER = "abort_user"  # interrupted by user (Ctrl+C)
