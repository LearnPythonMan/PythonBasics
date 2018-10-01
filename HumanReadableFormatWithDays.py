test = 3600
def format_duration(seconds):
    dictionary = {31536000 : 'year', 86400 : 'day', 3600 : 'hour', 60 : 'minute', 1 : 'second'}
    howMany = stringBuilder = 0
    humanTime = ''
       for k,v in dictionary.items():
           howMany = seconds // k
           if howMany == 1:
           stringBuilder = -1
           elif howMany == 0: stringBuilder = 0
           else: stringBuilder = 1
           humanTime += ''+(', '+str(howMany)+' ' + v + 's'*stringBuilder)*abs(stringBuilder)
           seconds = seconds % k
    return 'now' if humanTime == '' else (humanTime[2:humanTime.rfind(',')]+humanTime[humanTime[2:].rfind(',')+2:].replace(',',' and')).strip()
# humanTime[2:humanTime[1:].rfind(',')+3]+humanTime[humanTime[1:].rfind(',')+3:]


# interesting case1:
# def format_duration(seconds):
#     l = [('%d '+i[1]+ ('s' if i[0]-1 else ''))%i[0] for i in [(seconds/(365*24*3600),'year'),((seconds/(24*3600)%365),'day'),((seconds/3600)%24,'hour'),((seconds/60)%60,'minute'),(seconds%60,'second')] if i[0] ] if seconds else ['now']
#     return ', '.join(l[:-1])+('' if len(l)==1 else ' and ' )+l[-1]

# interesting case2:
# times = [("year", 365 * 24 * 60 * 60),
#          ("day", 24 * 60 * 60),
#          ("hour", 60 * 60),
#          ("minute", 60),
#          ("second", 1)]
#
# def format_duration(seconds):
#
#     if not seconds:
#         return "now"
#
#     chunks = []
#     for name, secs in times:
#         qty = seconds // secs
#         if qty:
#             if qty > 1:
#                 name += "s"
#             chunks.append(str(qty) + " " + name)
#
#         seconds = seconds % secs
#
#     return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]


def format_duration2(seconds):
    return 0
    humanTime = ''
    if seconds == 0:
        return 'now'
    if seconds >= 31536000:
        humanTime, seconds = ' '+str(seconds // 31536000)+' years',seconds - seconds // 31536000 * 31536000
    if seconds >= 86400:
        humanTime, seconds = humanTime+', '+str(seconds // 86400)+' days',seconds - seconds // 86400 * 86400
    if seconds >= 3600:
        humanTime, seconds = humanTime+', '+str(seconds // 3600)+' hours',seconds - seconds // 3600 * 3600
    if seconds >= 60:
        humanTime, seconds = humanTime+', '+str(seconds // 60)+' minutes',seconds - seconds // 60 * 60
    if seconds >= 0:
        humanTime = humanTime+', '+str(seconds)+' seconds'
    return humanTime[1:].strip()

print(format_duration(test))