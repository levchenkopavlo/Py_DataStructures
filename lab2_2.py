class History:

    def __init__(self):
        self.stack = []
        self.stack_forward = []

    def action(self, action):
        if action.startswith('url:'):
            self.stack.append(action)
            self.stack_forward = []
            print(f'{self.stack=}')
            print(f'{self.stack_forward=}')
        elif action == 'back':
            self.stack_forward.append(self.stack.pop())
            print(f'{self.stack=}')
            print(f'{self.stack_forward=}')
        elif action == 'forward':
            self.stack.append(self.stack_forward.pop())
            print(f'{self.stack=}')
            print(f'{self.stack_forward=}')


actions = ['url:', 'back', 'forward']
history1 = History()
history1.action('url:ukr.net')
history1.action('url:ukr.net/mail')
history1.action('url:pravda.com.ua')
history1.action('back')
history1.action('back')
history1.action('forward')
history1.action('url:google.com.ua')
# base action
# new url
# back
# forward
