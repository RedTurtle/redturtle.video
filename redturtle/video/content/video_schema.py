from Products.Archetypes import atapi
from redturtle.video import videoMessageFactory as _

VIDEO_SCHEMA=atapi.Schema((

    atapi.StringField('year',
                widget = atapi.StringWidget(
                    label = _(u'label_year', default=u'Year'),
                    size=4,
                    maxlength=4,
                    description = '',
                    )),

    atapi.StringField('duration',
                widget = atapi.StringWidget(
                    label = _(u'label_duration', default=u'Duration'),
                    description = '',
                    )),

    atapi.BooleanField('useSplashScreen',
                default=False,
                schemata="look",
                widget = atapi.BooleanWidget(
                    label = _(u'label_use_imge', default=u'Use image as splash screen?'),
                    description = _(u'help_use_imge',
                                    default=u"Check for use splash screen image not only in the product's portlet "
                                            u"but also in the video view."),
                    )),

    atapi.TextField('text',
              required=False,
              searchable=True,
              validators = ('isTidyHtmlWithCleanup',),
              default_output_type = 'text/x-html-safe',
              widget = atapi.RichWidget(
                        label = _(u'label_body_text', default=u'Body Text'),
                        description = _(u'help_body_text',
                                        default=u'You can use this field for provide a video transcript'),
                        rows = 25,
                        )),

    atapi.IntegerField('width',
                validation=('isInt',),
                default_method="getDefaultWidth",
                schemata="look",
                widget = atapi.IntegerWidget(
                    label = _(u'label_width', default=u'Video width'),
                    description = '',
                    )),

    atapi.IntegerField('height',
                validation=('isInt',),
                default_method="getDefaultHeight",
                schemata="look",
                widget = atapi.IntegerWidget(
                    label = _(u'label_height', default=u'Video height'),
                    description = '',
                    )),

))
