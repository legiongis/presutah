define(['knockout', 'viewmodels/report'], function(ko, ReportViewModel) {
    return ko.components.register('easement_report', {
        viewModel: function(params) {
            params.configKeys = [];
            var self = this;
            // define params for custom report here

            ReportViewModel.apply(this, [params]);
            // Put custom report logic here
        },
        template: { require: 'text!report-templates/easement_report' }
    });
});
