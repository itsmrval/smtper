import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def test_smtp_server(host, port, username, password, use_tls, use_ssl, from_address, to_address, subject, body):
    try:
        if use_ssl:
            print("Testing server in with SSL")
            server = smtplib.SMTP_SSL(host, port)
        else:
            print("Testing server without SSL")
            server = smtplib.SMTP(host, port)

        if use_tls:
            print("Using TLS")
            server.starttls()
        print("Logging in...")
        server.login(username, password)

        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        print("Sending email...")
        server.sendmail(from_address, to_address, msg.as_string())
        print("Email sent!")

    except Exception as e:
        print(f"An error occured: {e}")
    finally:
        server.quit()

host = ""
port = 25
username = ""
password = ""

from_address = ""
to_address = ""

subject = "SMTP test script - tmp.internal@scaleway.com"
body = "This is a test email from the smtp script."

# w/ nothing
test_smtp_server(host, port, username, password, False, False, from_address, to_address, subject, body)

# w/ TLS
test_smtp_server(host, port, username, password, True, False, from_address, to_address, subject, body)

# w/ SSL
test_smtp_server(host, 465, username, password, True, True, from_address, to_address, subject, body)
