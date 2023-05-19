'''
uid를 이용해 추적, 관리하고 있다가 최종 닉네임만 출력하기
'''
def solution(record):
    name = {} # uid => name
    log = [] # (uid, action)
    for action in record:
        action = parse_action(action)
        if action['type'] == 'Enter' or action['type'] == 'Change':
            name[action['uid']] = action['name']
        if action['type'] != 'Change':
            log.append((action['uid'], action['type']))
    print(name)
    print(log)
    return list(map(lambda x: log_to_str(x, name), log))

def log_to_str(log, namemap):
    uid, action = log
    if action == 'Enter':
        action = '들어왔습니다'
    elif action == 'Leave':
        action = '나갔습니다'
    return f'{namemap[uid]}님이 {action}.'

def parse_action(action):
    action = action.split(' ')
    if action[0] == 'Enter' or action[0] == 'Change':
        return {'type': action[0], 'uid': action[1], 'name': action[2]}
    elif action[0] == 'Leave':
        return {'type': action[0], 'uid': action[1]}
    else:
        raise ValueError('not expected value on parse_action')
