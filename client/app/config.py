import os

class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "b'\\\xea\xfe`\xa0\x92\xd3\xb0\x06\xf3g#\xb8\xc0\xb5\xca(T\xa0/\xbc\x8dF\xc5'"
    SQLALCHEMY_DATABASE_URI = 'postgres://ycpxvmbgeaimqv:14ebfcb29772b612bf2a8dc25adc90966ed0c1ba720bd208a55c48d8242db896@ec2-3-231-46-238.compute-1.amazonaws.com:5432/d8lloj66mp1es6'
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_size' : 100, 'pool_recycle' : 280}
