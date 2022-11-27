import os
os.system("pip install git+https://github.com/AWeirdScratcher/linelib")
print("Installation has completed!")
if "REPLIT_DB_URL" in os.environ:
  print("Found replit environment!")
  print(">>> Let's start coding now! (main.py)")
  open("main.py", "w").write("# example\nfrom linelib import Client\n\nclient = Client('secret', 'token')\n\n@client.event('ready')\ndef ready():\n  print(\"I'm ready!\")\n\n\nclient.run(host='0.0.0.0', port=8080)")
else:
  print(">>> You can now start coding!")
