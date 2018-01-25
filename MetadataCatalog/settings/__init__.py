from MetadataCatalog.settings.base import *
from MetadataCatalog.settings.production import *

try:
    from MetadataCatalog.settings.development import *
except:
    pass
