from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        subprocess.Popen(
            ["/bin/bash", "/root/self-healing-infrastructure-devops/scripts/autoheal.sh"]
        )
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Auto-heal triggered")

server = HTTPServer(("0.0.0.0", 5001), Handler)
print("Webhook listener running on port 5001")
server.serve_forever()



Run with:

python3 scripts/webhook_server.py
