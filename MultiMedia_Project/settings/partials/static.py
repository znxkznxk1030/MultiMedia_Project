# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

import os
from .base import BASE_DIR, PROJECT_ROOT_DIR

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

DIRECT_ROOT = os.path.join(
    BASE_DIR,
    "dist",
    "media"
)


# Media files
MEDIA_ROOT = os.path.join(
    PROJECT_ROOT_DIR,
    "dist",
    "media",
)
MEDIA_URL = '/media/'