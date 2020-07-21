
```
# install customize font-ranger (add TC subset supports)
npm install git://github.com/livingbio/font-ranger.git#dev

# install required Python package
python3 -mvirtualenv venv
source ./venv/bin/activate

pip install -r requirements.txt
python3 convert.py jf-openhuninn-1.1/jf-openhuninn-1.1.ttf
```