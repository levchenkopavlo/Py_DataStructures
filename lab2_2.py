class History:

    def __init__(self):
        self.stack = []

    def action(self, action):
        if action.startswith('url:'):
            self.stack.append(action)


actions = ['url:', 'back', 'forward']
history1 = History()
history1.action('url:ukr.net')

# base action
# new url
# back
# forward
