from Products.CMFCore.utils import getToolByName
from hoshuko.helsinki.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone upgrades."""

    def setUp(self):
        self.portal = self.layer['portal']
        from plone.app.testing import TEST_USER_ID
        from plone.app.testing import setRoles
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_upgrades_0_to_1(self):

        mailhost = getToolByName(self.portal, 'MailHost')
        mailhost.smtp_host = 'smtp.mail.send'
        self.assertEqual(mailhost.smtp_host, 'smtp.mail.send')

        properties = getToolByName(self.portal, 'portal_properties')
        site_properties = getattr(properties, 'site_properties')
        site_properties.manage_changeProperties(webstats_js='')
        self.failIf(site_properties.getProperty('webstats_js'))

        from hoshuko.helsinki.upgrades import upgrade_0_to_1
        upgrade_0_to_1(self.portal)

        self.assertEqual(mailhost.smtp_host, 'smtp.nebula.fi')

        self.assertEqual(
            site_properties.getProperty('webstats_js'),
            '<script type="text/javascript">\n\nvar _gaq = _gaq || [];\n_gaq.push([\'_setAccount\', \'UA-789306-7\']);\n_gaq.push([\'_trackPageview\']);\n\n(function() {\nvar ga = document.createElement(\'script\'); ga.type = \'text/javascript\'; ga.async = true;\nga.src = (\'https:\' == document.location.protocol ? \'https://ssl\' : \'http://www\') + \'.google-analytics.com/ga.js\';\nvar s = document.getElementsByTagName(\'script\')[0]; s.parentNode.insertBefore(ga, s);\n})();\n\n</script>'
        )
