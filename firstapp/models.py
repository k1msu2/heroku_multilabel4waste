from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import os
import hashlib
from datetime import datetime

#def upload_to_id_image(instance, filename):
#    extension = '.jpg'
#    path = 'train/%(filename)s_%(date_now)s/' % {'filename': filename, 'date_now': datetime.now().strftime("%Y%m%d%H%M%S")}
    #return '%(path)s%(extension)s' % {'path': path, 'extension': extension}

class Post(models.Model):
    image = ProcessedImageField(upload_to='train',
                                #processors=[ResizeToFill(500, 500)],
                                format='JPEG'
                                #options={'quality': 60}
                                )
    
#    image = ProcessedImageField(upload_to='train',
#                                processors=[ResizeToFill(500, 500)],
#                                format='JPEG',
#                                options={'quality': 60})