# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName
from hoshuko.helsinki.tests.base import IntegrationTestCase
class TestSetup(IntegrationTestCase):

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_hoshuko_helsinki_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('hoshuko.helsinki'))

    ## properties.xml
    def test_portal_title(self):
        self.assertEquals("ヘルシンキ日本語補習校 -- Helsingin Japanilainen Kouluyhdistys", self.portal.getProperty('title'))

    def test_portal_email_from_address(self):
        self.assertEquals("helsinki@hoshuko.info", self.portal.getProperty('email_from_address'))

    def test_portal_email_from_name(self):
        self.assertEquals("Helsingin Japanilainen Kouluyhdistys", self.portal.getProperty('email_from_name'))

    ## actions.xml
    def test_sitemap_action_installed(self):
        self.failUnless('sitemap' not in self.portal.portal_actions.site_actions.objectIds())

    def test_accessibility_action_installed(self):
        self.failUnless('accessibility' in self.portal.portal_actions.site_actions.objectIds())

    def test_contact_action_installed(self):
        self.failUnless('contact' in self.portal.portal_actions.site_actions.objectIds())

    def test_plone_setup_action_installed(self):
        self.failUnless('plone_setup' in self.portal.portal_actions.site_actions.objectIds())

    def test_login_action_installed(self):
        self.failUnless('login' in self.portal.portal_actions.site_actions.objectIds())

    def test_logout_action_installed(self):
        self.failUnless('logout' in self.portal.portal_actions.site_actions.objectIds())

    ### user
    def test_preferences_removed(self):
        self.failUnless('preferences' not in self.portal.portal_actions.user.objectIds())

    def test_dashboard_removed(self):
        self.failUnless('dashboard' not in self.portal.portal_actions.user.objectIds())

    ## language
    def test_available_languages(self):
        ltool = getToolByName(self.portal, 'portal_languages')
        self.assertEquals('ja', ltool.getDefaultLanguage())
        self.assertEqual([('ja', u'Japanese')], ltool.listSupportedLanguages())

    def test_default_language(self):
        portal_properties = getToolByName(self.portal, 'portal_properties')
        site_properties = portal_properties.get('site_properties')
        self.assertEquals('ja', site_properties.getProperty('default_language'))
