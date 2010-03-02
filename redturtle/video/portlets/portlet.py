from zope.interface import implements
from zope.component import getMultiAdapter, queryMultiAdapter

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from zope import schema
from zope.formlib import form

from plone.memoize.instance import memoize

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.vocabularies.catalog import SearchableTextSourceBinder
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget

from Products.ATContentTypes.interface import IATTopic, IATFolder

from redturtle.video.interfaces import IRTVideo
from collective.flowplayer.interfaces import IFlowPlayerView
from redturtle.video import videoMessageFactory as _

from Products.CMFCore.utils import getToolByName


def getImageUrl(resource):
    if ((IRTVideo.providedBy(resource) and \
                resource.hasSplashScreenImage()) or \
                    (not IRTVideo.providedBy(resource) and \
                                    resource.hasSplashScreenImage)):
        if not IRTVideo.providedBy(resource):
            return resource.getURL()+'/image_thumb'
        return resource.absolute_url()+'/image_thumb'
    portal = getToolByName(resource, 'portal_url').getPortalObject()
    return portal.absolute_url() +\
                "/++resource++collective.flowplayer.css/play.png"


class IRTVideoPortlet(IPortletDataProvider):
    """A portlet which can display video gallery"""

    header = schema.TextLine(title = _(u"label_portlet_header",
                                        default = u"Portlet header"),
                             description = _(u"help_portlet_header",
                                 default = u"Title of the rendered portlet"),
                             required = True)

    target = schema.Choice(title = _(u"label_target_object",
                                        default = u"Target object"),
                           description = _(u"help_target_object",
                                        default = u"This can be a file "\
                                            "containing an video content, "\
                                            "or a folder or collection "\
                                            "containing videos"),
                           required = True,
                           source = SearchableTextSourceBinder(
                                      {'object_provides': [IATTopic.__identifier__,
                                            IATFolder.__identifier__,
                                            IRTVideo.__identifier__]},
                                      default_query = 'path:'))

    limit = schema.Int(title = _(u"label_number_of_videos_to_show",
                            default = u"Number of videos to show"),
                       description = _(u"help_number_of_videos_to_show",
                            default = u"Enter a number greater than 0 "\
                                    "to limit the number of items displayed"),
                       required = False,
                       default = 0)

    show_more = schema.Bool(title = _(u"label_show_more_link",
                                default=u"Show more... link"),
                       description = _(u"help_show_more_link",
                                    default = u"If enabled, a more... "\
                                        "link will appear in the footer of "\
                                        "the portlet, "
                                    "linking to the underlying data."),
                       required = True,
                       default = True)


class Assignment(base.Assignment):
    implements(IRTVideoPortlet)

    header = u""
    target = None
    limit = 0
    show_more = False

    def __init__(self, header=u"", target=None, limit=None, show_more=False):
        self.header = header
        self.target = target
        self.limit = limit
        self.show_more = show_more

    @property
    def title(self):
        return _(u"Video gallery: ") + self.header


class Renderer(base.Renderer):
    render = ViewPageTemplateFile('portlet.pt')

    @property
    def available(self):
        return len(self.videos()) > 0

    def target_url(self):
        target = self.target()
        if target is None:
            return None
        else:
            return target.absolute_url()

    @memoize
    def videos(self):
        target = self.target()
        limit = self.data.limit
        if target is None:
            return []
        if IRTVideo.providedBy(target):
            return [dict(title=target.Title(),
                         description=target.Description(),
                         url=target.absolute_url(),
                         year=target.getYear(),
                         duration=target.getDuration(),
                         image_url=getImageUrl(target)),
                   ]
        if IATFolder.providedBy(target):
            values = []
            videos = target.getFolderContents(
                        contentFilter = {'object_provides':
                                            IRTVideo.__identifier__})
            for v in videos:
                values.append(dict(title = v.Title,
                                   description = v.Description,
                                   url = v.getURL(),
                                   year = v.getYear,
                                   duration = v.getDuration,
                                   image_url = getImageUrl(v),
                                   ))
            return (limit and values[:limit]) or values

        if IATTopic.providedBy(target):
            values = []
            videos = target.queryCatalog(
                    contentFilter={'object_provides':
                                    IRTVideo.__identifier__})
            for v in videos:
                values.append(dict(title=v.Title,
                                   description=v.Description,
                                   url=v.getURL(),
                                   year=v.getYear,
                                   duration=v.getDuration,
                                   image_url=getImageUrl(v),
                                   ))
            return (limit and values[:limit]) or values
        return []

    @memoize
    def target(self):
        target_path = self.data.target
        if not target_path:
            return None

        if target_path.startswith('/'):
            target_path = target_path[1:]

        if not target_path:
            return None

        portal_state = getMultiAdapter((self.context, self.request),
                                            name=u'plone_portal_state')
        portal = portal_state.portal()
        return portal.restrictedTraverse(target_path, default=None)


class AddForm(base.AddForm):
    form_fields = form.Fields(IRTVideoPortlet)
    form_fields['target'].custom_widget = UberSelectionWidget

    label = _(u"label_add_video_portlet",
                    default = u"Add Video Portlet")
    description = _(u"help_add_video_portlet",
                        default = u"This portlet display a video gallery.")

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    form_fields = form.Fields(IRTVideoPortlet)
    form_fields['target'].custom_widget = UberSelectionWidget

    label = _(u"label_edit_video_portlet",
                default = u"Edit Video Portlet")
    description = _(u"help_edit_video_portlet",
                default = u"This portlet display a video gallery.")
