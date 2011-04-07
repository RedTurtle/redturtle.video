from Products.Archetypes import atapi
from redturtle.video import videoMessageFactory as _

VIDEO_SCHEMA=atapi.Schema((

    atapi.StringField('year',
                widget = atapi.StringWidget(
                    label = _(u'label_year', default=u'Year'),
                    description = '',
                    )),

    atapi.StringField('duration',
                widget = atapi.StringWidget(
                    label = _(u'label_duration', default=u'Duration'),
                    description = '',
                    )),
                    
    atapi.BooleanField('useSplashScreen',
                default=False,
                schemata="Look",
                widget = atapi.BooleanWidget(
                    label = _(u'label_use_imge', default=u'Use image as splash screen?'),
                    description = _(u'help_use_imge',
                                    default=u"Check for use splash screen image not only in the product's portlet "
                                            u"but also in the video view."),
                    )),

    atapi.IntegerField('width',
                validation=('isInt',),
                default=251,
                schemata="Look",
                widget = atapi.IntegerWidget(
                    label = _(u'label_width', default=u'Video width'),
                    description = '',
                    )),

    atapi.IntegerField('height',
                validation=('isInt',),
                default=200,
                schemata="Look",
                widget = atapi.IntegerWidget(
                    label = _(u'label_height', default=u'Video height'),
                    description = '',
                    )),

))
