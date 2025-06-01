import http.server
import socketserver
import cgi
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

PORT = 8000

# The HTML page served for "/"
INDEX_HTML = b"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>AES Encrypt/Decrypt</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-900 text-white flex flex-col items-center justify-center min-h-screen p-4">
  <h1 class="text-3xl font-bold mb-6">AES Encryption / Decryption</h1>

  <textarea id="text" rows="4" class="w-full max-w-xl p-2 mb-4 text-black" placeholder="Enter text here..."></textarea>
  <input id="key" type="text" class="w-full max-w-xl p-2 mb-4 text-black" placeholder="Enter key (min 16 chars)" />

  <div class="space-x-4 mb-4">
    <button onclick="processAES('encrypt')" class="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded">Encrypt</button>
    <button onclick="processAES('decrypt')" class="bg-green-600 hover:bg-green-700 px-4 py-2 rounded">Decrypt</button>
  </div>

  <h2 class="text-xl font-semibold mb-2">Result:</h2>
  <textarea id="result" rows="4" readonly class="w-full max-w-xl p-2 text-black"></textarea>

  <script>
    async function processAES(action) {
      const text = document.getElementById('text').value.trim();
      const key = document.getElementById('key').value.trim();
      if (!text || !key) {
        alert('Please enter both text and key');
        return;
      }
      const data = new URLSearchParams();
      data.append('action', action);
      data.append('text', text);
      data.append('key', key);

      try {
        const response = await fetch('/aes', {
          method: 'POST',
          body: data
        });
        const result = await response.text();
        document.getElementById('result').value = result;
      } catch (e) {
        alert('Error: ' + e.message);
      }
    }
  </script>
</body>
</html>
"""

class AESHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.send_header('Content-length', str(len(INDEX_HTML)))
            self.end_headers()
            self.wfile.write(INDEX_HTML)
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/aes':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            form = cgi.parse_qs(post_data.decode('utf-8'))
            action = form.get('action', [''])[0]
            text = form.get('text', [''])[0]
            key = form.get('key', [''])[0]

            # Prepare key bytes (16, 24, or 32 bytes for AES)
            key_bytes = key.encode('utf-8')
            if len(key_bytes) < 16:
                key_bytes = key_bytes.ljust(16, b'\0')
            elif 16 < len(key_bytes) < 24:
                key_bytes = key_bytes.ljust(24, b'\0')
            elif 24 < len(key_bytes) < 32:
                key_bytes = key_bytes.ljust(32, b'\0')
            else:
                key_bytes = key_bytes[:32]

            try:
                if action == 'encrypt':
                    cipher = AES.new(key_bytes, AES.MODE_CBC)
                    ct_bytes = cipher.encrypt(pad(text.encode('utf-8'), AES.block_size))
                    result = b64encode(cipher.iv + ct_bytes).decode('utf-8')
                elif action == 'decrypt':
                    data = b64decode(text)
                    iv = data[:16]
                    ct = data[16:]
                    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
                    pt = unpad(cipher.decrypt(ct), AES.block_size)
                    result = pt.decode('utf-8')
                else:
                    result = 'Invalid action'
            except Exception as e:
                result = f'Error: {str(e)}'

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(result.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

with socketserver.TCPServer(("", PORT), AESHandler) as httpd:
    print(f"Serving AES encrypt/decrypt server at http://localhost:{PORT}")
    httpd.serve_forever()
