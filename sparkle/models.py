import os
import zipfile
import tempfile
import shutil
import plistlib
from django.db import models
from django.conf import settings
from sparkle.conf import SPARKLE_PRIVATE_KEY_PATH

class Application(models.Model):
    """A sparkle application"""
    
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Version(models.Model):
    """A version for a given application"""
    
    application = models.ForeignKey(Application)
    
    title = models.CharField(max_length=100)
    version = models.CharField(blank=True, null=True, max_length=10)
    short_version = models.CharField(blank=True, null=True, max_length=50)
    dsa_signature = models.CharField(blank=True, null=True, max_length=80)
    length = models.CharField(blank=True, null=True, max_length=20)
    release_notes = models.TextField(blank=True, null=True)
    minimum_system_version = models.CharField(blank=True, null=True, max_length=10)
    published = models.DateTimeField(auto_now_add=True)
    update = models.FileField()
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
        
    def save(self, *args, **kwargs):
                
        # if there is no dsa signature and a private key is provided in the settings
        if not self.dsa_signature and SPARKLE_PRIVATE_KEY_PATH and os.path.exists(SPARKLE_PRIVATE_KEY_PATH):
            command = 'openssl dgst -sha1 -binary < "%s" | openssl dgst -dss1 -sign "%s" | openssl enc -base64' % (path, SPARKLE_PRIVATE_KEY_PATH)
            process = os.popen(command)
            self.dsa_signature = process.readline().strip()
            process.close()

        # Calculate file size
        if not self.length :
            # TODO: set correct size
            self.length = 0

        super(Version, self).save(*args, **kwargs)

class SystemProfileReport(models.Model):
    """A system profile report"""
    
    ip_address = models.GenericIPAddressField()
    added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return u'SystemProfileReport'
    
class SystemProfileReportRecord(models.Model):
    """A key/value pair for a system profile report"""
    
    report = models.ForeignKey(SystemProfileReport)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=80)
    
    def __unicode__(self):
        return u'%s: %s' % (self.key, self.value)
