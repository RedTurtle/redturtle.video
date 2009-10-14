from Products.Archetypes import atapi
from redturtle.video import videoMessageFactory as _

VIDEO_SCHEMA=atapi.Schema((
        
    atapi.StringField('year',
                searchable=True,
                widget = atapi.StringWidget(
                    label = _(u'label_year', default=u'Year'),
                    description = '',
                    )),

    atapi.StringField('duration',
                searchable=True,
                widget = atapi.StringWidget(
                    label = _(u'label_duration', default=u'Duration'),
                    description = '',
                    )),
))
