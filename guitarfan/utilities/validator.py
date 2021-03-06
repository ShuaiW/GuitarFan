#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import current_app
from wtforms.validators import ValidationError

def catch_errors(errors):
    messages = ''
    if errors:
        for (field, errors) in errors.items()[::-1]:
            for error in errors:
                messages = '%s;%s' % (messages, error)

    return messages[1:] if messages else None


class Unique(object):
    """ validator that checks field uniqueness """
    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        self.message = message if message else u'The current element value is already in use'

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data).first()
        id = form.id.data if 'id' in form else None
        if check and (id is None or id != check.id):
            raise ValidationError(self.message)


class UnChange(object):
    """ validator that checks field unchange """
    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        self.message = message if message else u'The current element can not be modified'

    def __call__(self, form, field):
        check = self.model.query.filter_by(id=form.id.data).first()
        if check is not None and field.data != getattr(check, self.field):
            raise ValidationError(self.message)


class AllowedPhotoFile(object):
    """ validator that checks upload file """
    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        self.message = message if message else u'Upload photo file is not available format'

    def __call__(self, form, field):
        if field.data:
            allowed_extenstions = current_app.config['ARTIST_PHOTO_ALLOWED_EXTENSIONS']
            filename = field.data.filename
            if not ('.' in filename and filename.rsplit('.', 1)[1] in allowed_extenstions):
                raise ValidationError(self.message)