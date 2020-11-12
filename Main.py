from project import app
import os

print("in main")

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
