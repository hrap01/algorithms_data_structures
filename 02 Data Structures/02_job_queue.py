import heapq


class JobDescription:

    def __init__(self, thread_id, release_time=0):
        self.thread_id = thread_id
        self.release_time = release_time

    def __lt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id < other.thread_id
        return self.release_time < other.release_time


class JobQueue:

    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.size = m
        assert m == self.size

    def job_assignment(self):
        self.result = []
        self.job_insert = [JobDescription(i) for i in range(self.num_workers)]

        for i in self.jobs:
            worker = heapq.heappop(self.job_insert)

            self.result.append((worker.thread_id, worker.release_time))

            worker.release_time += i
            heapq.heappush(self.job_insert, worker)

    def output(self):
        for i, x in self.result:
            print(i, x)

    def solve(self):
        self.read_data()
        self.job_assignment()
        self.output()


if __name__ == "__main__":
    job_queue = JobQueue()
    job_queue.solve()
