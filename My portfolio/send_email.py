import smtplib  # This module defines an SMTP (Simple Mail Transfer Protocol)
# client session,
# which is used to send emails
import ssl  # This module provides secure (TLS/SSL) connections,


# which are needed for securely connecting to email servers.

def send_email(message, user_email):
    host = "smtp.gmail.com"
    port = 465
    username = "indranilde92@gmail.com"
    password = "wkjj yqdk ymcx hvop"
    receiver = user_email
    context = ssl.create_default_context()  # Creates a secure SSL context for
    # encrypting the connection between your Python
    # script and the Gmail server.

    with smtplib.SMTP_SSL(host=host, port=port,
                          context=context) as server:  # Establishes a secure connection to the Gmail SMTP server using SSL.
        server.login(username, password)
        server.sendmail(username, receiver, message)
