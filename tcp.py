# Copyright 2012 Google Inc. All Rights Reserved.

"""One-line documentation for tcp module.

A detailed description of tcp.
"""

__author__ = 'gboland@google.com (Gary Boland)'


import paramiko

def main(argv):
   try:
    target = socket.gethostbyname(argv[1])
  except KeyError:
    print >>sys.stderr, 'Give me a hostname, master.'
    sys.exit(-1)


  buf = 1024
  s = socket.socket(socket.AF_INET, socket.SOCK_STEAM)
  if target_system.startswith('17'):
    s.connect(target_system, 22)
  else:
    proxy = ('172.20.8.21', 6309)
    s.connect(proxy)
    s.send("proxy1 %s:22 ssh ssh1 luser mcjeff ruser root\r\n" % target)

  t = transport.Transport(s)
  t.start_client()

  print t.get_remote_server_key()


if __name__ == '__main__':
  main()
