from constants import app, redis, db
from model import Device

db.create_all()

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')

@app.route('/record')
def recode():
    deviceinfo = Device("ddddddeee","0.0.1", "1", 100)
    db.session.add(deviceinfo)
    db.session.commit()
    return 'OK'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
