
#!/bin/bash

git pull

date > version

git add version
git commit -m "Version updated."

git push 


