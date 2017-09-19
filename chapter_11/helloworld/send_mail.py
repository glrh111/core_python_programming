from google.appengine.api import mail
from google.appengine.api import app_identity

import webapp2

# https://cloud.google.com/appengine/docs/standard/python/mail/sending-mail-with-mail-api
# sudo ln -s /usr/sbin/sendmail /usr/bin/sendmail

def send_approved_mail(sender_address, receiver):
    # [START send_mail]
#     mail.send_mail(sender=sender_address,
#                    to=receiver,
#                    subject="Your account has been approved",
#                    body="""Dear:
# Your example.com account has been approved.  You can now visit
# http://www.example.com/ and sign in using your Google Account to
# access new features.
# Please let us know if you have any questions.
# The example.com Team
# """)

    message = mail.EmailMessage(
        sender=sender_address,
        subject="Your account has been approved")

    message.to = receiver
    message.body = """Dear Lao Wang:

    Your example.com account has been approved.  You can now visit
    http://www.example.com/ and sign in using your Google Account to
    access new features.

    Please let us know if you have any questions.

    The example.com Team
    """
    message.send()


class SendMailHandler(webapp2.RequestHandler):
    def get(self):

        r = self.request.params

        receiver = r.get('r', '')

        if receiver:
            send_approved_mail('{}@appspot.gserviceaccount.com'.format(
                app_identity.get_application_id()), receiver)

        self.response.content_type = 'text/plain'
        self.response.write('r for receivers. \nTo: {}'.format(receiver) + str(r.items()))


app = webapp2.WSGIApplication([
    ('/send_mail', SendMailHandler),
], debug=True)