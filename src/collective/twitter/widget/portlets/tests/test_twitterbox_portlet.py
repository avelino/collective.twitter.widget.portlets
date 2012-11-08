# -*- coding: utf-8 -*-

import unittest2 as unittest

from collective.twitter.widget.portlets.testing import INTEGRATION_TESTING

from zope.component import getUtility, getMultiAdapter

from plone.portlets.interfaces import IPortletType
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletAssignment
from plone.portlets.interfaces import IPortletDataProvider
from plone.portlets.interfaces import IPortletRenderer

from plone.app.portlets.storage import PortletAssignmentMapping

from collective.twitter.widget.portlets import twbox

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles


class TwitterBoxTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_portlet_addview_registered(self):
        portlet = getUtility(
            IPortletType,
            name='collective.twitter.widget.portlets.TwitterBoxPortlet')

        self.assertEqual(portlet.addview,
                          'collective.twitter.widget.portlets'
                          '.TwitterBoxPortlet')

    def test_portlet_title_registered(self):
         portlet = getUtility(
                 IPortletType,
                 name='collective.twitter.widget.portlets.TwitterBoxPortlet')

         self.assertEqual(u"Twitter Widget", portlet.title)

