import multiprocessing, gevent
bind = "127.0.0.1:8000"

pidfile = "/tmp/blog.pid"
workers = multiprocessing.cpu_count()*2 + 1  
