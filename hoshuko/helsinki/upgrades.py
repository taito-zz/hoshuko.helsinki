from Products.CMFCore.utils import getToolByName

import logging


PROFILE_ID = 'profile-hoshuko.helsinki:default'


def upgrade_0_to_1(context, logger=None):
    """Reimport mailhost.xml and propertiestool.xml."""
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger(__name__)

    logger.info('Reimporting mailhost.xml.')
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(
        PROFILE_ID,
        'mailhost',
        run_dependencies=False,
        purge_old=False,
    )
    logger.info('Reimported mailhost.xml.')

    logger.info('Reimporting propertiestool.xml.')
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(
        PROFILE_ID,
        'propertiestool',
        run_dependencies=False,
        purge_old=False,
    )
    logger.info('Reimported propertiestool.xml.')
