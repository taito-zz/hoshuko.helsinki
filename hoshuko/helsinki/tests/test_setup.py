# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from hoshuko.helsinki.tests.base import IntegrationTestCase


class TestSetup(IntegrationTestCase):

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_hoshuko_helsinki_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('hoshuko.helsinki'))

    def test_is_Maps_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('Maps'))

    def test_is_plonetheme_terrafirma_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('plonetheme.terrafirma'))

    def test_mailhost__smtp_host(self):
        mailhost = getToolByName(self.portal, 'MailHost')
        self.assertEqual(mailhost.smtp_host, 'smtp.nebula.fi')

    def test_mailhost__smtp_port(self):
        mailhost = getToolByName(self.portal, 'MailHost')
        self.assertEqual(mailhost.smtp_port, 25)

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-hoshuko.helsinki:default'),
            u'1'
        )

    ## properties.xml
    def test_portal_title(self):
        self.assertEquals("ヘルシンキ日本語補習校 -- Helsingin Japanilainen Kouluyhdistys", self.portal.getProperty('title'))

    def test_portal_email_from_address(self):
        self.assertEquals("helsinki@hoshuko.info", self.portal.getProperty('email_from_address'))

    def test_portal_email_from_name(self):
        self.assertEquals("Helsingin Japanilainen Kouluyhdistys", self.portal.getProperty('email_from_name'))

    def test_propertiestool__webstats_js(self):
        properties = getToolByName(self.portal, 'portal_properties')
        site_props = properties.site_properties
        self.assertEqual(
            site_props.getProperty('webstats_js'),
            '<script type="text/javascript">\n\nvar _gaq = _gaq || [];\n_gaq.push([\'_setAccount\', \'UA-789306-7\']);\n_gaq.push([\'_trackPageview\']);\n\n(function() {\nvar ga = document.createElement(\'script\'); ga.type = \'text/javascript\'; ga.async = true;\nga.src = (\'https:\' == document.location.protocol ? \'https://ssl\' : \'http://www\') + \'.google-analytics.com/ga.js\';\nvar s = document.getElementsByTagName(\'script\')[0]; s.parentNode.insertBefore(ga, s);\n})();\n\n</script>'
        )

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
