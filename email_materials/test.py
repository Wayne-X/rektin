import yagmail

yag = yagmail.SMTP('dabindan@gmail.com', 'd4d34c66d8')

to = 'dabindan@gmail.com'
subject = 'yagmail wooo'
body = list()
body.append('does this work???')
body.append('resume.pdf')

yag.send(to = to, subject = subject, contents = body)