# -*- coding: utf-8 -*-
from zope.interface import implements
from zope.interface import alsoProvides

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from zope import schema
from zope.component import getUtility

from zope.formlib import form
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.registry.interfaces import IRegistry
from zope.schema.interfaces import IContextSourceBinder
from collective.prettydate.interfaces import IPrettyDate

from collective.twitter.widget.portlets import _
from collective.twitter.widget.portlets.config import PROJECTNAME

from zope.security import checkPermission

from plone.memoize import ram
from time import time

from DateTime import DateTime

import json
import urllib

import logging

logger = logging.getLogger(PROJECTNAME)


class ITwitterBoxPortlet(IPortletDataProvider):
    """A portlet

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """

    data_id = schema.TextLine(title=_(u'Data Widget ID'),
            description=_(u"Create new Widget in "
                u"https://twitter.com/settings/widgets and input ID"))


class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(ITwitterBoxPortlet)

    data_id = u""

    def __init__(self, data_id=u"",):

        self.data_id = data_id


class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    render = ViewPageTemplateFile('twbox.pt')

    def getDataId(self):
        """
        Returns the header for the portlet
        """
        return self.data.data_id


class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    form_fields = form.Fields(ITwitterBoxPortlet)

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(ITwitterBoxPortlet)
