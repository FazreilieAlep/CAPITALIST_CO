SECRET_KEY = 'django-insecure-a%lupt7%xxzz4z3gbmb07_2y$iy3c)%bek#rv(b2j2=6^^u-jw'
DEBUG = True

LOGGING['formatters']['colored'] = {  # type: ignore # noqa: F821
    '()':
    'colorlog.ColoredFormatter',
    'format':
    '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s'
}

LOGGING['loggers']['core']['level'] = 'DEBUG'  # type: ignore # noqa: F821
LOGGING['handlers']['console']['level'] = 'DEBUG'  # type: ignore # noqa: F821
LOGGING['handlers']['console'][
    'formatter'] = 'colored'  # type: ignore # noqa: F821
