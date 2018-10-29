import itchat, time

itchat.auto_login(True)  ###登录，扫码，相当于登录微信网页版

# WANT_TO_SAY = '祝%s狗年旺旺，身体健康！！'
WANT_TO_SAY = input('输入要群发的消息：')

friendList = itchat.get_friends(update=True)[1:]
i = 0
for friend in friendList:
    i += 1
    # print('第%d个    ' % (i), WANT_TO_SAY % (friend['DisplayName'] or friend['NickName']))
    print('第%d个' % (i), WANT_TO_SAY, friend['DisplayName'] or friend['NickName'])
    # itchat.send(WANT_TO_SAY % (friend['DisplayName'] or friend['NickName']))
    itchat.send(WANT_TO_SAY)
    time.sleep(.3)
