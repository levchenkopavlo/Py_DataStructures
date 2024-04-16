from queue import Queue


class BankQueue:
    def __init__(self):
        self.queue = Queue()

    def put_client(self, client):
        self.queue.put(client)

    def serve_next_client(self):
        if self.queue.empty():
            print('no client')
            return
        client = self.queue.get()

        print(f'ви обслуговуєте клієнта {client}')

    def number_client(self):
        return self.queue.qsize()

    def is_empty_queue(self):
        return self.queue.empty()



bank_queue = BankQueue()
bank_queue.put_client('Mary')
bank_queue.put_client('Sophy')

bank_queue.serve_next_client()
bank_queue.put_client('John')
bank_queue.serve_next_client()
bank_queue.serve_next_client()
bank_queue.serve_next_client()