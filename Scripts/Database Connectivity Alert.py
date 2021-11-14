#!/usr/bin/env python
# -- ############################################################################
# -- #      Copyright (C) 2020-2021 Vivek Kumar <vivekkumar.xda@gmail.com>      #
# -- #                All rights reserved.                                      #
# -- ############################################################################
# -- #
# -- # Project          : ETL Alerts
# -- # Application      : DBConnectivityAlert
# -- # File Name        : DBConnectivityAlert.py
# -- # Exec Method      : Jython ODI Script
# -- # Description      : This Script made to automatically send alert mail
# -- #                    when any db link is down
# -- #
# -- # Change History
# -- # -----------------------------------------------------------------------
# -- # Version     Date             Author                      Remarks
# -- # =======  ===========     =============               ============================
# -- # 1.0      17-July-2021     Vivek Kumar                Initial Version
# -- #
# -- ############################################################################

from java.sql import SQLException
# Import the email modules we'll need
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Import smtplib for the actual sending function
import smtplib

# Function to check the connectivity


def get_connectivity(p_link_name):
    l_query = "SELECT COUNT(1) FROM DUAL@%s " % (p_link_name)
    l_count = 0
    try:
        result = sql_stmt.executeQuery(l_query)
        try:
            while result.next():
                l_count = result.getInt(1)
            result.close()

        except SQLException, se:
            raise 'Inner Exception with query : %s - %s' % (l_query, e)
            return l_count

        return l_count
    except Exception, e:
        raise 'Outer Exception with query : %s - %s' % (l_query, e)
        return l_count


def send_mail(TO, SUBJECT, BODY):
    # Create a text/plain message
    MSG = MIMEMultipart()

    MSG['Subject'] = SUBJECT
    MSG['From'] = "ETLAlertTeam"
    MSG['To'] = TO
    MSG.attach(MIMEText(BODY, 'plain'))

    # Send the message via our own SMTP server, but don't include the envelope header.
    server = smtplib.SMTP(host="00.000.000.244", port=25)
    server.sendmail(MSG['From'], MSG['To'], MSG.as_string())
    server.quit()


# Form the DB connection
src_conn = odiRef.getJDBCConnection("SRC")
sql_stmt = src_conn.createStatement()

# Form the DB Links list
db_links = ["DB_LINK1", "DB_LINK2", "DB_LINK3"]
# get the status of DB Links
db_links_status = [(link, get_connectivity(link)) for link in db_links]
# get the DB links which failed
db_links_error = [values[0] for values in db_links_status if 0 in values]
# View the latest status
print(db_links_status)
print(db_links_error)

# Form the email message if there is any error
mail_body = None
mail_subject = None

# If DB Link Matrix has errors send email
if len(db_links_error) > 0:
    mail_subject = "Critical !!! DWH DB Link Down"
    mail_body = "Hi Team,\n \n\
                The below DB Link connectivity has been broken. \
                Please contact Database Administrator. \n \n"
    for i, link in enumerate(db_links_error):
        mail_body += "\t"+str(i+1)+".\t"+link+"\n"
    mail_body += "\n \nThanks,\
                        \nETL Team"
    print(mail_body)
    send_mail("email_id@domin.com", mail_subject, mail_body)

# Close the connection
sql_stmt.close()
src_conn.close()
