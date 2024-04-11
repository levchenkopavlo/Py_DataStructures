class History:

    def __init__(self):
        self.stack = []
        self.stack_forward = []

    def action(self, action):
        if action.startswith('url:'):
            self.stack.append(action)
            self.stack_forward = []
        elif action == 'back':
            self.stack_forward.append(self.stack.pop())
        elif action == 'forward':
            self.stack.append(self.stack_forward.pop())


actions = ['url:', 'back', 'forward']
history1 = History()
history1.action('url:ukr.net')
history1.action('url:ukr.net/mail')

# base action
# new url
# back
# forward
