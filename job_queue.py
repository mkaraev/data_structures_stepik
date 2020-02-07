# python3

from heapq import heappop, heappush, heapify
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
FreeWorker = namedtuple("FreeWorker", ["time", "worker"])


def assign_jobs(n_workers, jobs):
    result = []
    queue = []
    for i in range(n_workers):
        queue.append(FreeWorker(0, i))
    heapify(queue)

    for job in jobs:
        next_free_time, worker = heappop(queue)
        result.append(AssignedJob(worker, next_free_time))
        heappush(queue, FreeWorker(next_free_time + job, worker))

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
