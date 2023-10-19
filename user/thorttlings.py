from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

class Anon5ForMinute(AnonRateThrottle):
    scope = '5_for_minute'


class User10ForMinute(UserRateThrottle):
    scope = '10_for_minute'
