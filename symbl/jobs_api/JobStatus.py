from enum import Enum

class JobStatus(Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    FAILED = "failed"
    COMPLETED = "completed"

    def __eq__(self, other): 
        if not isinstance(other, JobStatus):
            # don't attempt to compare against unrelated types
            raise ValueError("Can not compare JobStatus type object with {} type object".format(type(other)))

        return self.value == other.value