#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2, urllib
import mimetools
import mimetypes
import itertools
class httpclient:
    def __init__(self):
        pass
    def get(self,url):
        try:
            return urllib2.urlopen(url).read()
        except Exception as e:
            print e
            return ''
    def post(self,url,data):
        try:
            return urllib2.urlopen(url,data).read()
        except Exception as e:
            print e
            return ''
class MultiPartForm(object):
    """Accumulate the data to be used when posting a form."""

    def __init__(self):
        self.form_fields = []
        self.files = []
        self.boundary = mimetools.choose_boundary()
        return
    
    def get_content_type(self):
        return 'multipart/form-data; boundary=%s' % self.boundary

    def add_field(self, name, value):
        """Add a simple field to the form data."""
        self.form_fields.append((name, value))
        return

    def add_file(self, fieldname, filename, fileHandle, mimetype=None):
        """Add a file to be uploaded."""
        body = fileHandle.read()
        if mimetype is None:
            mimetype = mimetypes.guess_type(filename)[0] or 'multipart/form-data'
        self.files.append((fieldname, filename, mimetype, body))
        return
    def __str__(self):
        """Return a string representing the form data, including attached files."""
        # Build a list of lists, each containing "lines" of the
        # request.  Each part is separated by a boundary string.
        # Once the list is built, return a string where each
        # line is separated by '\r\n'.  
        parts = []
        part_boundary = '--' + self.boundary
        
        # Add the form fields
        parts.extend(
        [ part_boundary,
        'Content-Disposition: form-data; name="%s"' % name,
        '',
        str(value),
        ]
        for name, value in self.form_fields
        )
        
            # Add the files to upload
        parts.extend(
        [ part_boundary,
          'Content-Disposition: file; name="%s"; filename="%s"' % \
          (field_name, filename),
          'Content-Type: %s' % content_type,
          '',
          body,
          ]
        for field_name, filename, content_type, body in self.files
        )
        
        # Flatten the list and add closing boundary marker,
        # then return CR+LF separated data
        flattened = list(itertools.chain(*parts))
        flattened.append('--' + self.boundary + '--')
        flattened.append('')
        for item in flattened:
            print item
            print "\n"
        return '\r\n'.join(flattened)
    
            
        
    
