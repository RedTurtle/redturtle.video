"""Test setup for integration and functional tests.

When we import PloneTestCase and then call setupPloneSite(), all of
Plone's products are loaded, and a Plone site will be created. This
happens at module level, which makes it faster to run each test, but
slows down test runner startup.
"""
import os
from Products.Five import zcml
from Products.Five import fiveconfigure

from Testing import ZopeTestCase as ztc

from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

from zope.publisher.interfaces.browser import IHTTPRequest
from zope.publisher.browser import TestRequest
from zope.interface import implements

@onsetup
def setup_product():
    """Set up the package and its dependencies.

    The @onsetup decorator causes the execution of this body to be
    deferred until the setup of the Plone site testing layer. We could
    have created our own layer, but this is the easiest way for Plone
    integration tests.
    """

    # Load the ZCML configuration for the example.tests package.
    # This can of course use <include /> to include other packages.

    fiveconfigure.debug_mode = True
    import redturtle.video
    zcml.load_config('configure.zcml', redturtle.video)
    fiveconfigure.debug_mode = False

    # We need to tell the testing framework that these products
    # should be available. This can't happen until after we have loaded
    # the ZCML. Thus, we do it here. Note the use of installPackage()
    # instead of installProduct().
    # This is *only* necessary for packages outside the Products.*
    # namespace which are also declared as Zope 2 products, using
    # <five:registerPackage /> in ZCML.

    # We may also need to load dependencies, e.g.:
    #   ztc.installPackage('borg.localrole')

    ztc.installPackage('redturtle.video')

# The order here is important: We first call the (deferred) function
# which installs the products we need for this product. Then, we let
# PloneTestCase set up this product on installation.

setup_product()
ptc.setupPloneSite(products=['redturtle.video'])

class TestRequest(TestRequest):
    implements(IHTTPRequest)


class TestCase(ptc.PloneTestCase):
    """We use this base class for all the tests in this package. If
    necessary, we can put common utility or setup code in here. This
    applies to unit test cases.
    """

    def getVideoFile(self):
        video = '/'.join(os.path.realpath( __file__ ).split(os.path.sep )[:-2])
        video = '%s/tests/1-2-3.mp4' % video
        fd = open(video, 'rb')
        data = fd.read()
        fd.close()
        return data


class FunctionalTestCase(ptc.FunctionalTestCase):
    """We use this class for functional integration tests that use
    doctest syntax. Again, we can put basic common utility or setup
    code in here.
    """

    def afterSetUp(self):
        roles = ('Member', 'Contributor')
        self.portal.portal_membership.addMember('contributor',
                                                'secret',
                                                roles, [])

    def getImage(self):
        image = '/'.join(os.path.realpath( __file__ ).split(os.path.sep )[:-2])
        image = '%s/tests/plone_logo.png' % image
        fd = open(image, 'rb')
        data = fd.read()
        fd.close()
        return data

    def getVideoFile(self):
        video = '/'.join(os.path.realpath( __file__ ).split(os.path.sep )[:-2])
        video = '%s/tests/1-2-3.mp4' % video
        fd = open(video, 'rb')
        data = fd.read()
        fd.close()
        return data

