# import email.message, smtplib
#
# apology = email.message.Message()
# apology.add_header('To', 'leopold.moz@pythonchallenge.com')
# apology.add_header('From', from_addr)
# apology.add_header('Subject', 'Apology')
# apology.set_payload('Sorry!')
#
# server = smtplib.SMTP_SSL('smtp.gmail.com')
# server.login(from_addr, pw)
# server.sendmail(apology['from'], apology['to'], apology.as_string())
# server.quit()

# Re: my broken zip Re: Apology
#
# Leopold Mozart
#
# Never mind that.
#
# Have you found my broken zip?
#
# md5: bbb8b499a0eef99b52c7f13f4e78c24b
#
# Can you believe what one mistake can lead to?
import hashlib
import zipfile

with open('maze/mybroken.zip', 'rb') as f:
    broken_data = f.read()

repaired = False
for b in range(len(broken_data)):
    if repaired:
        break
    for i in range(256):
        try_repair = broken_data[:b] + bytes((i,)) + broken_data[b + 1:]
        if 'bbb8b499a0eef99b52c7f13f4e78c24b' == hashlib.md5(try_repair).hexdigest():
            print(b, i)
            with open('maze/repaired.zip', 'wb') as f:
                f.write(try_repair)
            repaired = True
            break

with zipfile.ZipFile('maze/repaired.zip', 'r') as f:
    for file in f.namelist():
        f.extract(file, 'maze')  # speed
# text for challenge #26 is 'Hurry up, I'm missing the boat' --> speedboat
