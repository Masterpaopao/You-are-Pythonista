import time 
from collections import namedtuple

def make_nametuple(line):
    l = line.split()
    mapping = {
        'remote_addr': lambda x: x,
        'time_local': lambda x: time.strftime('%Y-%m-%d %X',time.strptime(x.split()[0][1:],"%d/%b/%Y:%H:%M:%S")),
        'request_method': lambda x: eval(x).split()[0],
        'request_uri': lambda x: eval(x).split()[1],
        'request_agreement': lambda x: eval(x).split()[2],
        'status': lambda x: eval(x),
        'boby_bytes_sent': lambda x: eval(x),
        'http_referer' : lambda x: eval(x),
        'http_user_agent': lambda x: eval(x),
    }
    m_list = list(mapping.keys())
    Log = namedtuple('Log',m_list)

    log = Log(
        remote_addr = mapping['remote_addr'](l[0]),
        time_local = mapping['time_local'](" ".join(l[3:5])),
        request_method = mapping['request_method'](" ".join(l[5:8])),
        request_uri = mapping['request_uri'](" ".join(l[5:8])),
        request_agreement = mapping['request_agreement'](" ".join(l[5:8])),
        status = mapping['status'](l[8]),
        boby_bytes_sent = mapping['boby_bytes_sent'](l[9]),
        http_referer = mapping['http_referer'](l[10]),
        http_user_agent = mapping['http_user_agent'](" ".join(l[11:]))
    )

    return log

def main():
    with open('./access.log','r') as f:
        line = f.readline()
        print(make_nametuple(line))

if __name__ == "__main__":
    main()

    