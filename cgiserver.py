#!/usr/bin/env python3

from http.server import CGIHTTPRequestHandler, HTTPServer

handler = CGIHTTPRequestHandler
handler.cgi_directories = ['/', '/htbin']  # this is the default
server = HTTPServer(('localhost', 8000), handler)
server.serve_forever()