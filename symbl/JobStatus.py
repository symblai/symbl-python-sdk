from enum import Enum

class JobStatus(Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    FAILED = "failed"
    COMPLETED = "completed"