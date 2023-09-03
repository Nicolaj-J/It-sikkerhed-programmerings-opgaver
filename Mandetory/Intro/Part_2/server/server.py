import socket
import re
import logging
import sys
from datetime import datetime
import calendar
import os

folder = os.getcwd()
index = f"{folder}\\server\\index.html"
not_found = f"{folder}\\server\\notfound.html"

# Log setup
logging.basicConfig(filename='server/server.log', filemode='w', format='%(message)s')


def get_length(msg):
    msg_len = len(str(msg).encode())
    return msg_len


def index_msg():
    rsp_code = "200"
    http_header = f"HTTP/1.1 {rsp_code} OK\r\n\r\n"
    with open(index, "r") as f:
        index_txt = f.read()
    f.close()
    response = http_header + index_txt
    return response, rsp_code


def html_req(splitted):
    try:
        rsp_code = "200"
        http_header = f"HTTP/1.1 {rsp_code} OK\r\n\r\n"
        html_other = f"{folder}\\server\\{splitted}"
        with open(html_other, "r") as f:
            html_txt = f.read()
        f.close()
        response = http_header + html_txt
        return response, rsp_code
    except:
        return not_found_msg()


def bad_request():
    rsp_code = "400"
    response = f"HTTP/1.1 {rsp_code} Bad Request\r\n\r\n"
    return response, rsp_code


def not_found_msg():
    rsp_code = "404"
    http_header = f"HTTP/1.1 {rsp_code} Not Found\r\n\r\n"
    with open(not_found, "r") as f:
        not_found_txt = f.read()
    f.close()
    print(not_found_txt)
    response = http_header + not_found_txt
    return response, rsp_code


# Local port and IP Socket settings
port = 12004
ip = socket.gethostbyname(socket.gethostname())
print(ip)
addr = (ip, port)

# Server socket object defined
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)

# Server listens for new connection attemps
server.listen(1)


def get_date():
    pass


while True:
    try:
        conn, addr = server.accept()
        msg = conn.recv(2048).decode("utf-8")
        # Standard/first HTTP Request

        if re.search(r"GET \/ HTTP\/1.\d{1}", msg):
            request = re.findall(r"GET \/ HTTP\/1.\d{1}", msg)[0]
            return_msg, rsp_code = index_msg()
            conn.send(return_msg.encode())

        # Get request for html file
        elif re.search(r"GET .*.html HTTP\/1.\d{1}", msg):
            request = re.findall(r"GET .*.html HTTP\/1.\d{1}", msg)[0]
            splitted = request.split(" ")[1]
            return_msg, rsp_code = html_req(splitted)
            conn.send(return_msg.encode())

        # HTTP Request for element (not html)
        elif re.search(r"GET .* HTTP\/1.\d{1}", msg):
            request = re.findall(r"GET .* HTTP\/1.\d{1}", msg)[0]
            return_msg, rsp_code = not_found_msg()
            conn.send(return_msg.encode())

        # Request not recognised
        else:
            request = msg.splitlines()[0]
            return_msg, rsp_code = bad_request()
            conn.send(return_msg.encode())
        print(msg)  # Debug
        # Log call return_msg rsp_code
        date = f"[{datetime.now().day}/{calendar.month_abbr[datetime.now().month]}/{datetime.now().year}:{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second} +0100]"
        logging.warning(f'{addr[0]} - - {date} "{request}" {rsp_code} {get_length(return_msg)}')
        # conn.send(str(msg).encode())
        conn.close()
    except KeyboardInterrupt:
        sys.exit()
