import multiprocessing

debug = True
daemon = False
bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1
forwarded_allow_ips = '*'

