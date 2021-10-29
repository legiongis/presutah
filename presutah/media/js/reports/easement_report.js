define([
'underscore',
'knockout',
'knockout-mapping',
'viewmodels/report',
'arches',
'knockstrap',
'bindings/chosen',
'geojson-extent',
'views/components/map',
'views/components/cards/select-feature-layers',
], function(_, ko, koMapping, ReportViewModel, arches, geojsonExtent, MapComponentViewModel, selectFeatureLayersFactory) {
    return ko.components.register('easement_report', {
        viewModel: function(params) {
            var self = this;

            // image carousel
            params.configKeys = ['nodes'];
            ReportViewModel.apply(this, [params]);


            // map params


            // Put custom report logic here
            self.imgs = ko.computed(function() {
                var imgs = [];
                var nodes = ko.unwrap(self.nodes);
                self.tiles().forEach(function(tile) {
                    _.each(tile.data, function(val, key) {
                        val = koMapping.toJS(val);
                        if (Array.isArray(val)) {
                            val.forEach(function(item) {
                                if (item.status &&
                                    item.type &&
                                    item.status === 'uploaded' &&
                                    item.type.indexOf('image') > -1 &&
                                    _.contains(nodes, key)
                                ) {
                                    imgs.push({
                                        src: (arches.urls.url_subpath + ko.unwrap(item.url)).replace('//', '/'),
                                        alt: item.name
                                    });
                                }
                            });
                        }
                    }, self);
                }, self);
                if (imgs.length === 0) {
                    imgs = [{
                        src: arches.urls.media + 'img/photo_missing.png',
                        alt: ''
                    }];
                }
                return imgs;
            });
            var widgets = [];
            var getCardWidgets = function(card) {
                widgets = widgets.concat(card.model.get('widgets')());
                card.cards().forEach(function(card) {
                    getCardWidgets(card);
                });
            };
            ko.unwrap(self.report.cards).forEach(getCardWidgets);
            this.nodeOptions = ko.observableArray(
                widgets.map(function(widget) {
                    return widget.node;
                }).filter(function(node) {
                    return ko.unwrap(node.datatype) === 'file-list';
                })
            );


        },
        template: { require: 'text!report-templates/easement_report' }
    });
});
