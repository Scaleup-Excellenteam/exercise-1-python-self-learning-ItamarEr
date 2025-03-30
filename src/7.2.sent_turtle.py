class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, title, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str title: The message title.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'title': title,
            'body': message_body,
            'sender': sender,
            'unread': True      # Message is unread by default
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self,username:str, n=None):
        """Read messages from a user's inbox.

        :param str username: The username of the user whose inbox to read.
        :param int n: The number of messages to read.
        :return: List of the messages.
        :rtype: list
        """
        if username not in self.boxes:
            print('User not found')
            return []
        if n is None:
            n = len(self.boxes[username])
        if n <= 0:
            return []

        user_box = self.boxes[username]
        unread_messages = [message for message in user_box if message['unread']]

        # Change the first n unread messages to read
        for message in unread_messages[:n]:
            message['unread'] = False

        return unread_messages[:n]

    def search_inbox(self,username:str, search_term:str) -> list:
        """Search messages in a user's inbox.

        :param str username: The username of the user whose inbox to search.
        :param str search_term: The term to search for in the messages.
        :return: List of the messages.
        :rtype: list
        """
        if username not in self.boxes:
            print('User not found')
            return []
        search_term = search_term.lower()    
        user_box = self.boxes[username]
        return [message for message in user_box if search_term in message['body'].lower()
                or search_term in message['title'].lower()]
