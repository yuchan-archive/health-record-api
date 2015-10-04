from constants import db

class Device(db.Model):
    __tablename__ = 'device'
    id = db.Column(db.Integer, primary_key=True)
    deviceid = db.Column(db.String(255), unique=False)
    stepnumber = db.Column(db.Integer, unique=False)
    version = db.Column(db.String(255), unique=False)
    buildnumber = db.Column(db.String(255), unique=False)

    def __init__(self, deviceid, version, buildnumber, stepnumber):
        self.deviceid = deviceid
        self.version = version
        self.buildnumber = buildnumber
        self.stepnumber = stepnumber

    def __repr__(self):
        return '<deviceid %r>' % self.deviceid
